# ECHO Web Application

A modern, responsive web application for ECHO - an AI-powered hearing health technology platform.

## Features

- 🎨 Modern, animated UI with dark/light theme toggle
- 📱 Fully responsive mobile-first design
- 📧 Contact form with data storage in CSV/Excel
- 📬 Newsletter subscription system
- 👥 Team member profiles with social links
- 🗺️ Interactive roadmap
- ❓ FAQ section
- 🎯 Future features showcase

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the project files**

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask server:**
   ```bash
   python app.py
   ```

4. **Open the application:**
   - Open `index.html` in your web browser
   - Or navigate to `http://localhost:5000` if using Flask template

## Data Storage

The application automatically creates the following files in a `data/` directory:

- `contact_submissions.csv` - Contact form submissions
- `contact_submissions.xlsx` - Contact form data in Excel format
- `newsletter_subscriptions.csv` - Newsletter email subscriptions

## Form Functionality

### Contact Form
- **Fields:** Name, Email, Message
- **Storage:** CSV and Excel files
- **Validation:** All fields required
- **Response:** Success/error messages displayed

### Newsletter Subscription
- **Field:** Email address
- **Storage:** CSV file
- **Validation:** Email format and duplicate check
- **Response:** Success/error messages displayed

## File Structure

```
ECHO-WEB/
├── index.html              # Main HTML file
├── app.py                  # Flask server
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── data/                  # Data storage directory (auto-created)
│   ├── contact_submissions.csv
│   ├── contact_submissions.xlsx
│   └── newsletter_subscriptions.csv
└── [image files]          # Team member photos and other assets
```

## Social Links

All team member social links are now properly configured:
- **LinkedIn:** Opens in new tab
- **GitHub:** Opens in new tab
- **Footer social links:** All working with proper URLs

## Theme Toggle

The theme toggle button in the footer now works properly:
- Switches between light and dark modes
- Saves preference in localStorage
- Updates all theme toggles simultaneously

## Troubleshooting

### Social Links Not Working
- Ensure all links have `target="_blank"` and `rel="noopener noreferrer"`
- Check that CSS z-index is properly set

### Form Submissions Not Working
- Make sure Flask server is running (`python app.py`)
- Check browser console for network errors
- Verify server is running on `http://localhost:5000`

### Data Files Not Created
- Ensure Python has write permissions in the project directory
- Check that `data/` directory is created automatically

## Technologies Used

- **Frontend:** HTML5, CSS3, JavaScript (ES6+)
- **Backend:** Python Flask
- **Data Storage:** CSV, Excel (pandas)
- **Styling:** Bootstrap 5, Custom CSS
- **Icons:** Bootstrap Icons

## Development

To modify the application:

1. **Frontend changes:** Edit `index.html`
2. **Backend changes:** Edit `app.py`
3. **Styling changes:** Modify CSS within `index.html`
4. **Add new features:** Update both frontend and backend as needed

## Support

For issues or questions:
- Check the browser console for JavaScript errors
- Verify all dependencies are installed
- Ensure the Flask server is running
- Check file permissions for data storage
