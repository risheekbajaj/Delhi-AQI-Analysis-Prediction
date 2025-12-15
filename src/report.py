import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf_report(output_filename, figures_dir):
    """
    Generates a PDF report summarizing the analysis and visualizations.
    
    Args:
        output_filename (str): Path to save the PDF (e.g., 'outputs/reports/Delhi_AQI_Report.pdf').
        figures_dir (str): Directory containing the generated PNG images.
    """
    # Ensure the directory for the report exists
    report_dir = os.path.dirname(output_filename)
    if report_dir and not os.path.exists(report_dir):
        os.makedirs(report_dir)

    doc = SimpleDocTemplate(output_filename, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # 1. Title
    story.append(Paragraph("The Air Quality Story of Delhi", styles['Title']))
    story.append(Spacer(1, 12))

    # 2. Objective
    story.append(Paragraph("<b>1. Objective</b>", styles['Heading2']))
    story.append(Paragraph(
        "The goal of this project is to analyze air quality trends in Delhi (2021-2024), "
        "understand the impact of various pollutants, and predict future AQI levels using machine learning.",
        styles['BodyText']
    ))
    story.append(Spacer(1, 12))

    # 3. Key Insights (Fixed Bullet Points)
    story.append(Paragraph("<b>2. Key Insights & Conclusion</b>", styles['Heading2']))
    
    insights = [
        "<b>Seasonality:</b> Air quality significantly worsens in Winter (Nov-Jan) due to temperature inversion and lower wind speeds.",
        "<b>Major Pollutants:</b> PM2.5 and PM10 are the primary contributors to poor AQI and are highly correlated.",
        "<b>Prediction:</b> The Random Forest model forecasts a recurring pattern of 'Severe' AQI in the upcoming winter months.",
        "<b>Recommendation:</b> Stricter pollution control measures are needed specifically during the pre-winter months (Oct-Nov)."
    ]
    
    for item in insights:
        # Use a bullet character manually
        p = Paragraph(f"• {item}", styles['BodyText'])
        story.append(p)
        story.append(Spacer(1, 6))
    
    story.append(Spacer(1, 12))

    # 4. Visualizations
    story.append(Paragraph("<b>3. Visualizations</b>", styles['Heading2']))
    
    # List of images to include (filename, description)
    images_to_plot = [
        ('aqi_trend.png', 'Long-term Daily AQI Trend'),
        ('monthly_aqi.png', 'Average Monthly AQI'),
        ('seasonal_aqi.png', 'Seasonal AQI Distribution'),
        ('correlation_heatmap.png', 'Correlation Matrix of Pollutants'),
        ('aqi_forecast.png', '12-Month AQI Forecast')
    ]

    for img_name, description in images_to_plot:
        img_path = os.path.join(figures_dir, img_name)
        
        if os.path.exists(img_path):
            story.append(Paragraph(f"<b>{description}:</b>", styles['Heading3']))
            # Resize image to fit page (width=400 keeps aspect ratio usually okay for standard plots)
            try:
                story.append(Image(img_path, width=400, height=200))
                story.append(Spacer(1, 12))
            except Exception as e:
                print(f"Error loading image {img_name}: {e}")
        else:
            print(f"Warning: Image not found at {img_path}")

    # Build PDF
    try:
        doc.build(story)
        print(f"PDF Report generated successfully: {output_filename}")
    except Exception as e:
        print(f"Failed to generate PDF: {e}")

# Example usage block (for testing independently)
if __name__ == "__main__":
    # Assumes default structure
    generate_pdf_report('../outputs/reports/Delhi_AQI_Report.pdf', '../outputs/figures/')