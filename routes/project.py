import os
import uuid
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from werkzeug.utils import secure_filename
from extensions import db
from models.project import Project
from models.contact import Contact

project_bp = Blueprint('project', __name__)

# ── helpers ───────────────────────────────────────────────────────────────────

def allowed_file(filename):
    return (
        '.' in filename and
        filename.rsplit('.', 1)[1].lower()
        in current_app.config['ALLOWED_EXTENSIONS']
    )

def save_image(file):
    """Save uploaded image; return relative path or None."""
    if not file or file.filename == '':
        return None
    if not allowed_file(file.filename):
        return None
    ext      = secure_filename(file.filename).rsplit('.', 1)[1].lower()
    filename = f"{uuid.uuid4().hex}.{ext}"
    upload_dir = current_app.config['UPLOAD_FOLDER']
    os.makedirs(upload_dir, exist_ok=True)
    file.save(os.path.join(upload_dir, filename))
    return f"images/uploads/{filename}"

# ── routes ────────────────────────────────────────────────────────────────────

@project_bp.route('/')
def index():
    featured = Project.query.order_by(Project.created_at.desc()).limit(6).all()
    return render_template('index.html', projects=featured)


@project_bp.route('/projects')
def projects():
    category = request.args.get('category', '')
    query    = Project.query
    if category:
        query = query.filter(Project.category.ilike(f'%{category}%'))
    all_projects = query.order_by(Project.created_at.desc()).all()
    categories   = db.session.query(Project.category).distinct().all()
    categories   = [c[0] for c in categories]
    return render_template('projects.html',
                           projects=all_projects,
                           categories=categories,
                           selected=category)


@project_bp.route('/add-project', methods=['GET', 'POST'])
def add_project():
    if request.method == 'POST':
        title         = request.form.get('title', '').strip()
        category      = request.form.get('category', '').strip()
        budget        = request.form.get('budget', '0')
        delivery_days = request.form.get('delivery_days', '1')
        description   = request.form.get('description', '').strip()
        image_file    = request.files.get('image')

        if not title or not category:
            flash('Title and category are required.', 'error')
            return redirect(url_for('project.add_project'))

        image_path = save_image(image_file)

        project = Project(
            title         = title,
            category      = category,
            budget        = float(budget),
            delivery_days = int(delivery_days),
            description   = description,
            image         = image_path,
        )
        db.session.add(project)
        db.session.commit()
        flash('Project added successfully!', 'success')
        return redirect(url_for('project.projects'))

    return render_template('add_project.html')


@project_bp.route('/project/<int:project_id>')
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('project_detail.html', project=project)


@project_bp.route('/project/<int:project_id>/edit', methods=['GET', 'POST'])
def edit_project(project_id):
    project = Project.query.get_or_404(project_id)
    if request.method == 'POST':
        project.title         = request.form.get('title', project.title).strip()
        project.category      = request.form.get('category', project.category).strip()
        project.budget        = float(request.form.get('budget', project.budget))
        project.delivery_days = int(request.form.get('delivery_days', project.delivery_days))
        project.description   = request.form.get('description', project.description).strip()
        image_file            = request.files.get('image')
        new_image             = save_image(image_file)
        if new_image:
            project.image = new_image
        db.session.commit()
        flash('Project updated!', 'success')
        return redirect(url_for('project.project_detail', project_id=project.id))
    return render_template('add_project.html', project=project)


@project_bp.route('/project/<int:project_id>/delete', methods=['POST'])
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    flash('Project deleted.', 'info')
    return redirect(url_for('project.projects'))


@project_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name    = request.form.get('name', '').strip()
        email   = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()

        if not name or not email or not message:
            flash('All fields are required.', 'error')
            return redirect(url_for('project.contact'))

        entry = Contact(name=name, email=email, message=message)
        db.session.add(entry)
        db.session.commit()
        flash("Thanks! I'll get back to you soon.", 'success')
        return redirect(url_for('project.contact'))

    return render_template('contact.html')
