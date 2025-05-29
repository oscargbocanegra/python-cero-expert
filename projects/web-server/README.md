# Web Server Project

## 📖 Overview
A Python-based web server implementation for learning and understanding HTTP protocols and server architecture.

## 🚀 Features
- Custom HTTP server implementation
- Request/response handling
- Static file serving
- Basic routing capabilities

## 📋 Prerequisites
- Python 3.7+
- Basic understanding of HTTP protocols

## 🛠️ Installation

```bash
# Clone the repository
git clone <repository-url>
cd web-server

# Install dependencies (if any)
pip install -r requirements.txt
```

## 🎯 Usage

```bash
# Run the web server
python server.py

# Access the server
# Open your browser and navigate to http://localhost:8000
```

## 📁 Estructura de los Proyectos

```
python-cero-expert/
├── 📁 projects/
│   └── 📁 web-server/
│       ├── 📄 main.py           # Aplicación principal
│       ├── 📄 store.py          # Lógica de almacenamiento
│       ├── 📄 Dockerfile        # Imagen Docker
│       ├── 📄 docker-compose.yml
│       └── 📄 requeriments.txt
├── 📁 .github/
│   └── 📁 workflows/
│       └── 📄 web-server.yml    # CI/CD pipeline
└── 📄 README.md
```

## 🔧 Configuration
- Default port: 8000
- Default host: localhost
- Configuration can be modified in `config/settings.py`

## 🧪 Testing

```bash
# Run tests
python -m pytest tests/

# Manual testing
curl http://localhost:8000
```

## 📝 API Endpoints
- `GET /` - Home page
- `GET /static/<filename>` - Serve static files
- `GET /api/status` - Server status

## 🤝 Contributing
1. Fork the project
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License
This project is part of the Python Zero to Expert course.