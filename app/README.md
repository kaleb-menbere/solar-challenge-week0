# Solar Data Discovery Dashboard - README

## 🌟 Overview

The **Solar Data Discovery Dashboard** is an interactive web application built with Streamlit that enables cross-country solar farm analysis. Users can upload solar data files and explore solar irradiance trends, temperatures, and wind conditions through various visualizations and statistical summaries.

**Live Demo**: [https://kaleb-menbere.streamlit.app/](https://kaleb-menbere.streamlit.app/)

---

## 🚀 Features

### 📊 Data Analysis Capabilities
- **Summary Statistics**: Comprehensive statistical overview of solar data
- **GHI Trends**: Time-series visualization of Global Horizontal Irradiance
- **Boxplots**: Distribution analysis across different datasets
- **Top Regions**: Identification of highest-performing solar regions

### 🔧 Interactive Features
- **Multi-file Upload**: Support for multiple CSV file uploads
- **Dynamic Filtering**: Adjustable GHI range filters
- **Customizable Display**: Configurable number of top regions to display
- **Real-time Updates**: Instant visualization updates based on user inputs

### 📈 Visualization Tools
- Line charts for temporal trends
- Box plots for distribution comparison
- Interactive data tables
- Responsive design for various screen sizes

---

## 🛠️ Installation & Local Development

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Step 1: Clone or Download the Project
```bash
git clone https://github.com/kaleb-menbere/solar-challenge-week0
cd solar-dashboard
```

### Step 2: Install Dependencies
```bash
pip install streamlit pandas seaborn matplotlib
```

### Step 3: Run the Application
```bash
streamlit run app.py
```

### Step 4: Access the Dashboard
Open your browser and navigate to: `http://localhost:8501`

---

## 📁 Project Structure

```
solar-dashboard/
│
├── app.py                 # Main Streamlit application
├── utils.py              # Utility functions (data loading, processing)
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

---

## 📋 Usage Instructions

### 1. Data Upload
- Click "Browse files" in the sidebar
- Select one or more CSV files containing solar data
- Supported files: CSV format with columns like:
  - `Timestamp` (datetime)
  - `GHI` (Global Horizontal Irradiance)
  - Other solar-related metrics

### 2. Data Filtering
- Adjust the GHI range slider to filter data
- Set the number of top regions to display
- Filters apply across all visualizations

### 3. Exploring Tabs

#### 📊 Summary Stats
- View descriptive statistics for each dataset
- Includes count, mean, std, min, max, percentiles

#### 📈 GHI Trends
- Time-series line charts showing GHI patterns
- Multiple datasets displayed separately

#### 📦 Boxplots
- Distribution comparison across datasets
- Identify outliers and data spread

#### 🏆 Top Regions
- Ranked list of highest-performing timestamps
- Configurable number of top entries

---

## 🔧 Technical Requirements

### Required Python Packages
```python
streamlit>=1.28.0
pandas>=1.5.0
seaborn>=0.12.0
matplotlib>=3.7.0
```

### Data Format Requirements
CSV files should contain:
- `Timestamp` column (parsable datetime)
- `GHI` column (numeric values)
- Optional: Other solar-related metrics

### Example Data Structure
```csv
Timestamp,GHI,Temperature,WindSpeed
2023-01-01 08:00:00,450,25,3.2
2023-01-01 09:00:00,680,27,2.8
...
```

---

## 🌐 Deployment

This application is deployed on **Streamlit Community Cloud**:

**Live URL**: https://kaleb-menbere-solar-challenge-week0-appmain-xfeald.streamlit.app/

### Deployment Steps:
1. Push code to GitHub repository
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect GitHub repository
4. Deploy automatically

---

## 🎯 Use Cases

### For Solar Energy Companies
- Site selection analysis
- Performance benchmarking
- Regional comparison studies

### For Researchers
- Solar data pattern analysis
- Climate impact studies
- Renewable energy research

### For Students & Educators
- Data visualization learning
- Solar energy education
- Statistical analysis practice

---

## 🐛 Troubleshooting

### Common Issues

1. **File Upload Problems**
   - Ensure files are in CSV format
   - Check column names match requirements
   - Verify file encoding

2. **Visualization Errors**
   - Confirm data contains required columns
   - Check for missing or invalid values
   - Verify datetime format

3. **Performance Issues**
   - Reduce file size for large datasets
   - Clear cache: `Ctrl + R` (browser refresh)

### Getting Help
- Check the Streamlit documentation
- Review data format requirements
- Ensure all dependencies are installed

---

## 📄 License

This project was developed for the **MoonLight Energy Solutions Solar Data Discovery Challenge**.

### Developer
**Kaleb Menbere**

---

## 🔄 Version History

- **v1.0** (Initial Release)
  - Multi-file upload capability
  - Basic visualization tabs
  - Interactive filtering

---

## 📞 Support

For questions or issues regarding this dashboard:
1. Check this README for solutions
2. Verify your data format matches requirements
3. Ensure all dependencies are properly installed

---

*Last Updated: December 2023*