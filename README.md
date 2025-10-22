# Rakshak.ai - Women's Safety and Navigation App

## Overview
Rakshak.ai is a modern, secure, and AI-driven website designed to empower women commuters, students, night-shift workers, and families in India to travel safely and confidently. The application leverages AI-powered safe route mapping, real-time crowd density analysis, SOS automation, and live safety reporting, combining machine intelligence with community participation.

## Features
- **AI-Powered Safe Route Mapping**: Provides users with the safest routes based on real-time data.
- **Real-Time Crowd Density Analysis**: Displays crowd density to help users avoid risky areas.
- **SOS Automation**: Quick access to emergency services with a single tap or voice command.
- **Live Safety Reporting**: Community-driven feedback to enhance safety measures.

## Design Specifications
- **Color Palette**: 
  - Soft Purple (#7B61FF)
  - Teal (#1FC5A8)
  - White (#FFFFFF)
  - Graphite Gray (#2C2C2C)
  
- **Typography**: 
  - Headings: Poppins / Montserrat
  - Body: Open Sans / Inter

- **Layout**: 
  - Responsive and mobile-first design
  - Clean top navigation with a sticky menu
  - Scroll-based transitions and animations

## Project Structure
The project is organized into several key directories and files:

- **app.py**: Main entry point for the Streamlit application.
- **src/pages**: Contains individual page components for the application.
- **src/components**: Reusable UI components.
- **src/services**: Backend services for maps, Firebase, AI features, and notifications.
- **src/models**: Machine learning models and preprocessing scripts.
- **src/utils**: Utility functions and constants.
- **backend**: API and worker scripts for backend functionality.
- **infra**: Infrastructure configuration files for deployment.
- **tests**: Unit and integration tests for the application.
- **docs**: Documentation for architecture, design system, and deployment.

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd rakshak-streamlit
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   streamlit run app.py
   ```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For support or inquiries, please reach out to [support@rakshak.ai](mailto:support@rakshak.ai).