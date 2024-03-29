# Enhanced Real Estate Listings with Nearby Services Integration

This project aims to enrich the real estate search experience by integrating listings with information about nearby services such as schools, public transportation, and shops. This integration aims to provide potential renters and buyers with a more comprehensive understanding of what living in a particular property would be like, considering not just the property itself but also the surrounding neighborhood's amenities.

## Overview

### Objectives
- To collect and integrate real estate listings with data on nearby services, offering users a more detailed perspective on each listing.
- To create a searchable database that allows users to filter properties based on proximity to desired services.
- To develop a web application that presents this integrated data in an easily navigable format.

### Methodology
- **Data Collection**: We scraped real estate listings from Idealista and service information from Pagine Gialle, focusing on the city of Milan.
- **Data Preprocessing**: Listings and services data were cleaned and normalized to ensure consistency and accuracy.
- **Geolocation Integration**: We calculated the geographical coordinates for each listing and service, enabling spatial queries to find services within a specified distance from each property.
- **Database Design**: Utilized MongoDB to store and query spatial data, implementing a "nested" approach where each property document includes a list of nearby services.
- **Web Application Development**: Designed a prototype web application that allows users to view property listings alongside information about nearby services, with customizable search filters based on service type and distance.

## Key Technologies
- **Web Scraping Tools**: Selenium for automated browser interactions to bypass scraping protections.
- **Database**: MongoDB for storing and querying spatial data.
- **Geolocation Services**: Bing Maps API for converting addresses to geographical coordinates.
- **Web Development Frameworks**: (Not specified in the report but would typically include technologies like React for the frontend and Node.js for the backend.)

## Findings and Impact
- Successfully integrated over 4,300 real estate listings with detailed information on nearby services.
- Developed an application prototype that demonstrates the value of this integrated approach to real estate searching.
- Identified opportunities for further data sources and additional features like user reviews and service quality indicators.

## Future Directions
- Expansion to other cities and integration with additional real estate platforms.
- Enhanced user interface and experience in the web application, including personalized recommendations.
- Automatic updates for both listings and services data to keep the database current.

## Repository Contents
- Data collection and preprocessing scripts.
- Database schema and integration scripts.
- Prototype web application code.
- Documentation on the project methodology, findings, and setup instructions.

## Conclusion
This project represents a significant step forward in real estate search technology, offering users a more holistic view of potential homes. By considering the ecosystem of services surrounding a property, we aim to empower users to make more informed decisions that go beyond square footage and price.


For a more detailed look at our methodology, findings, and the web application prototype, please refer to the full project documentation included in this repository.
