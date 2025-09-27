# 🌱 AI-Powered LCA Analysis Tool

An intelligent Life Cycle Assessment (LCA) tool for analyzing the environmental impact of different metals, built with Flask and modern web technologies.

## 🚀 Features

- **Material Analysis**: Comprehensive environmental impact assessment for various metals (virgin and recycled)
- **Interactive Dashboard**: Beautiful, responsive UI with real-time charts and visualizations
- **Sustainability Scoring**: AI-driven scoring system for environmental impact assessment
- **Lifecycle Analysis**: Detailed breakdown of impact across different lifecycle stages
- **Comparison Tool**: What-if scenario analysis comparing virgin vs recycled materials
- **History Tracking**: Keep track of previous analyses

## 🔧 Technology Stack

- **Backend**: Flask 3.0.0, Python 3.8+
- **Frontend**: HTML5, Tailwind CSS, Chart.js
- **Template Engine**: Jinja2
- **Deployment**: Render (with gunicorn)

## 📁 Project Structure

```
lca/
├── app/
│   ├── __init__.py          # Flask app factory
│   └── routes.py            # Route handlers and view functions
├── data/
│   └── lca_data.py          # Environmental impact data and constants
├── utils/
│   └── calculations.py      # Utility functions for LCA calculations
├── templates/
│   ├── base.html            # Base template with common layout
│   ├── index.html           # Main form and history display
│   └── results.html         # LCA analysis results page
├── static/                  # Static files (CSS, JS, images)
├── config/                  # Configuration files
├── main.py                  # Application entry point
├── requirements.txt         # Python dependencies
├── render.yaml             # Render deployment configuration
└── README.md               # This file
```

## 🛠️ Local Development Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd lca
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables (optional)**
   ```bash
   # Create a .env file
   FLASK_DEBUG=True
   SECRET_KEY=your-secret-key-here
   HOST=0.0.0.0
   PORT=5000
   ```

5. **Run the application**
   ```bash
   python main.py
   ```

6. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

## 🌐 Deployment on Render

This project is configured for easy deployment on Render.

### Automatic Deployment

1. **Connect your GitHub repository** to Render
2. **Create a new Web Service** on Render
3. **Configure the service**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn main:app`
   - **Environment**: Python 3

### Manual Deployment

1. **Push your code** to a GitHub repository
2. **Create render.yaml** (already included)
3. **Deploy** using Render's dashboard

### Environment Variables for Production

Set these environment variables in Render:

```bash
FLASK_DEBUG=False
SECRET_KEY=your-production-secret-key
HOST=0.0.0.0
PORT=10000
```

## 📊 Usage Guide

### Analyzing Materials

1. **Select a Material**: Choose from available metals (aluminum, copper, steel, etc.)
2. **Enter Quantity**: Specify the amount in kilograms
3. **Analyze**: Click the analyze button to generate results

### Understanding Results

- **Sustainability Score**: Overall environmental impact score (0-100, higher is better)
- **Environmental Metrics**: Carbon footprint, water usage, and energy consumption
- **Lifecycle Breakdown**: Visual chart showing impact across different stages
- **Comparison Insights**: Recommendations for switching to more sustainable alternatives

### Available Materials

**Virgin Materials:**
- Aluminum, Copper, Steel, Zinc, Nickel, Tin, Lead, Gold, Silver

**Recycled Materials:**
- All above materials in recycled form

## 🔧 Configuration

### Environmental Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `FLASK_DEBUG` | Enable debug mode | `True` |
| `SECRET_KEY` | Flask secret key for sessions | `dev-key-change-in-production` |
| `HOST` | Server host | `0.0.0.0` |
| `PORT` | Server port | `5000` |

### Data Configuration

Material data and lifecycle impacts can be modified in `data/lca_data.py`:

```python
MATERIAL_DATA = {
    'material_name': {
        'carbon': float,  # kg CO2e per kg
        'water': float,   # m³ per kg
        'energy': float,  # kWh per kg
        'waste': float,   # kg waste per kg
        'score': int      # Environmental score (0-100)
    }
}
```

## 🧪 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Display main form and history |
| `/` | POST | Process LCA analysis |
| `/health` | GET | Health check endpoint |

## 🤝 Contributing

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add some amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Flask** team for the excellent web framework
- **Chart.js** for beautiful data visualizations
- **Tailwind CSS** for responsive design utilities
- **Render** for seamless deployment platform

## 📞 Support

If you encounter any issues or have questions:

1. **Check** the [Issues](../../issues) section
2. **Create** a new issue if needed
3. **Contact** the development team

## 🔄 Version History

- **v1.0.0** - Initial release with basic LCA functionality
- **v1.1.0** - Added modular structure and improved UI
- **v1.2.0** - Enhanced deployment configuration and documentation

---

**Built with ❤️ for sustainable technology decisions**
