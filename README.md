# 🚀 StudioAI – AI-Powered Project Creation Platform

StudioAI is a modern AI-powered web application designed to simplify the process of creating freelance project listings. Instead of manually writing lengthy project descriptions, clients can simply enter the project title, category, and required features, and StudioAI generates a professional, well-structured project description using Artificial Intelligence.

The platform helps clients create attractive project postings while allowing freelancers to browse available opportunities and contact clients for collaboration. Built with Flask, MySQL, and Groq AI, StudioAI combines modern web development with generative AI to deliver an efficient and user-friendly experience.

---

# 🌟 Features

* 🤖 AI-powered project description generation using Groq AI (Llama 3.3 70B)
* 📋 Create and publish freelance project listings
* 📂 View all available projects
* 🔍 Detailed project information page
* 📞 Contact section for client inquiries
* 💻 Responsive and clean user interface
* 🔐 Secure environment variable configuration for API keys
* ⚡ Fast AI-generated content with a modern backend

---

# 💡 How It Works

1. The client opens the **AI Description Generator**.
2. They enter the project title, category, and key features.
3. StudioAI sends this information to the **Groq AI API**.
4. The AI generates a professional project description within seconds.
5. The generated description can be copied and used while creating a new project listing.
6. Once published, freelancers can browse the projects and contact the client if they are interested.

This workflow reduces the time required to create high-quality project postings and improves the overall user experience.

---

# 🛠️ Tech Stack

## Frontend

* HTML5
* CSS3
* JavaScript

## Backend

* Python
* Flask
* SQLAlchemy

## Database

* MySQL

## Artificial Intelligence

* Groq API
* Llama 3.3 70B Versatile

## Development Tools

* Git
* GitHub
* Visual Studio Code

---

# 📂 Project Structure

```
StudioAI
│
├── app.py
├── config.py
├── extensions.py
├── requirements.txt
├── .gitignore
│
├── database/
│
├── models/
│   ├── project.py
│   └── contact.py
│
├── routes/
│   ├── project.py
│   └── ai.py
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── templates/
    ├── index.html
    ├── projects.html
    ├── add_project.html
    ├── ai_generator.html
    ├── contact.html
    └── project_detail.html
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/thanisha2060/StudioAI.git
```

Navigate to the project folder

```bash
cd StudioAI
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file and configure:

```env
SECRET_KEY=your_secret_key

DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=freelance_studio_ai

GROQ_API_KEY=your_groq_api_key
```

Run the application

```bash
python app.py
```

---


# 🎯 Future Enhancements

* User Authentication & Authorization
* Freelancer Registration
* Proposal Submission System
* Project Search & Filtering
* AI Budget Recommendation
* AI Timeline Estimation
* Email Notifications
* Admin Dashboard
* Project Analytics
* Saved Projects
* Dark Mode

---

# 📚 Learning Outcomes

This project helped me gain practical experience in:

* Full-Stack Web Development
* Flask Application Development
* REST API Integration
* MySQL Database Design
* SQLAlchemy ORM
* Environment Variable Management
* AI Integration using Groq API
* Prompt Engineering
* Responsive Web Design
* Git & GitHub Version Control

---

# 👩‍💻 Developer

**Thanisha Kanchan**

MCA Student | Python Developer | AI & Full-Stack Web Development Enthusiast

GitHub:
https://github.com/thanisha2060

---

# 📄 License

This project is created for educational, learning, and portfolio purposes.

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub.
