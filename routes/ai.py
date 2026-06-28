from flask import Blueprint, render_template, request, jsonify, current_app
from groq import Groq

ai_bp = Blueprint("ai", __name__)

CATEGORIES = [
    "Web Development",
    "Mobile App",
    "UI/UX Design",
    "Logo & Branding",
    "SEO & Marketing",
    "E-Commerce",
    "Data Analytics",
    "WordPress",
    "Video Editing",
    "Content Writing",
]


@ai_bp.route("/ai-generator")
def ai_generator():
    return render_template("ai_generator.html", categories=CATEGORIES)


@ai_bp.route("/api/generate-description", methods=["POST"])
def generate_description():

    if request.is_json:
        data = request.get_json()
    else:
        data = request.form.to_dict()

    title = data.get("title", "").strip()
    category = data.get("category", "").strip()
    features = data.get("features", "").strip()

    if not title or not category:
        return jsonify({
            "error": "Title and Category are required."
        }), 400

    api_key = current_app.config.get("GROQ_API_KEY")

    if not api_key:
        return jsonify({
            "error": "Groq API Key not found."
        }), 500

    client = Groq(api_key=api_key)

    prompt = f"""
You are a senior project manager working for a freelance marketplace.

Create a professional freelance project posting.

Project Title:
{title}

Category:
{category}

Features / Tech Stack:
{features if features else "Not specified"}

Generate the response using the following format:

Project Overview

Responsibilities

Required Skills

Deliverables

Timeline

Additional Notes

Requirements:

- Professional tone.
- Around 250-350 words.
- Use bullet points where appropriate.
- Make freelancers interested in applying.
- Do NOT invent technologies that are not mentioned.
- Return plain text only.
"""

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert freelance project description writer."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_completion_tokens=700
        )

        description = response.choices[0].message.content.strip()

        return jsonify({
            "description": description
        })

    except Exception as e:
        print(e)

        return jsonify({
            "error": str(e)
        }), 500