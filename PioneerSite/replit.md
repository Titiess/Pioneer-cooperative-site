# Pioneer Multi-Purpose Cooperative Society Ltd.

## Overview

Pioneer Cooperative is a microfinance marketing website built with Python Flask. The application serves as an informational platform and lead generation tool for a Nigerian microfinance cooperative society. It allows prospective borrowers to learn about loan products, view requirements, and submit loan applications and contact inquiries. All form submissions are stored in CSV files rather than a traditional database.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture

**Template Engine**: Jinja2 (Flask's built-in templating)
- Base template (`base.html`) with shared layout including header, navigation, footer, and flash message display
- Child templates extend base for consistent branding across all pages
- Responsive design using CSS Grid and custom CSS variables for theming
- Accessibility features including skip-to-content links and semantic HTML

**Static Asset Organization**:
- `/static/css/` - Custom CSS with CSS variables for design system (pine green theme)
- `/static/js/` - Minimal client-side JavaScript
- `/static/img/` - Logo and hero images (SVG and JPG)

**Design System**: CSS variables define a consistent color palette (pine greens, mint, cream, lime accent) applied throughout the site for branding consistency.

### Backend Architecture

**Web Framework**: Flask 3.0.3
- Lightweight Python web framework chosen for simplicity
- No authentication required (public marketing site)
- Session secret key configurable via environment variable with fallback

**Routing Strategy**: Simple route-per-page model
- Marketing pages: `/`, `/about`, `/loan-products`, `/requirements`, `/faq`
- Interactive pages: `/apply`, `/contact`, `/thank-you`
- GET requests render forms, POST requests process submissions

**Form Processing**: Server-side validation and CSV persistence
- Form data validated on submission
- Flash messages provide user feedback
- Redirect to thank-you page on success
- Form data preserved on validation errors

### Data Storage

**CSV-Based Persistence**: Flat-file storage instead of relational database
- `data/applications.csv` - Loan application submissions
- `data/contacts.csv` - Contact form submissions
- Headers auto-generated on first run if files don't exist
- `ensure_data_dir()` and `ensure_csv_headers()` initialize storage on startup

**Data Schema**:

Applications CSV columns:
- timestamp, first_name, last_name, dob, email, phone
- academic_qualification, service_documents
- guarantor_name, guarantor_occupation, consent

Contacts CSV columns:
- timestamp, name, email, message

**Rationale**: CSV chosen over database for:
- Simplicity (no DB setup/maintenance)
- Easy data export for manual processing
- Low volume of submissions expected
- No need for complex queries or relationships

**Trade-offs**:
- Pros: Zero configuration, portable, human-readable
- Cons: No data integrity constraints, no concurrent write protection, manual backup needed

### Session Management

**Flash Messaging**: Flask's session-based flash messages for user feedback
- Success/error messages displayed after form submissions
- Messages automatically cleared after display
- Categories supported for different styling (success, error, info)

### Security Considerations

**Secret Key**: Session secret configurable via `SESSION_SECRET` environment variable
- Falls back to `'dev-secret'` for development
- Used for signing session cookies and flash messages

**Form Security**: Basic protections implemented
- CSRF protection should be added for production (currently missing)
- Input validation performed server-side
- No file uploads to avoid injection risks

## External Dependencies

### Python Packages

**Flask** (3.0.3): Core web framework
- Handles routing, templating, request/response cycle
- Provides session management and flash messaging

**python-dotenv** (1.0.1): Environment variable management
- Loads `.env` file if present for configuration
- Enables environment-specific settings

### Third-Party Services

**None currently integrated**. The application is self-contained with no external API calls, payment processors, email services, or analytics platforms.

**Potential Future Integrations**:
- Email service (SendGrid, Mailgun) for application notifications
- Payment gateway for ₦5,000 documentation fee
- SMS service for applicant communication
- Analytics (Google Analytics) for traffic monitoring

### Static Assets

**Current Assets**:
- `/static/img/logo.svg` - Cooperative logo (placeholder SVG with lime checkmark and "PIONEER" text - can be replaced)
- `/static/img/hero.jpg` - Homepage hero background (professional stock photo - can be replaced)

**To Replace Branding**:
1. Upload your logo to `/static/img/logo.svg` (or use PNG/JPG and update the path in `base.html`)
2. Upload your hero image to `/static/img/hero.jpg`

### Deployment Configuration

**Runtime**: Python 3.11
- Entry point: `python main.py`
- Server binds to `0.0.0.0:5000` (required for Replit webview)
- Production deployment should use proper WSGI server (Gunicorn, uWSGI)

**Environment Variables**:
- `SESSION_SECRET` - Flask session secret key (currently using fallback 'dev-secret' for development)

## Recent Changes

**October 2, 2025**: Complete implementation
- Built full Flask application with all 8 routes (Home, About, Loan Products, Requirements, FAQ, Apply, Contact, Thank You)
- Implemented dark pine green design system with CSS variables
- Created responsive layout with sticky translucent header
- Added hero section with background image and overlay
- Implemented working forms with CSV storage and validation
- All pages tested and working correctly
- Server running on port 5000 with webview output

## Usage Notes

**To view form submissions**:
- Open `/data/applications.csv` for loan applications
- Open `/data/contacts.csv` for contact form submissions

**To customize the design**:
- Edit `/static/css/styles.css` to change colors, spacing, or layout
- CSS variables at the top of the file control the entire color scheme

**To add more content**:
- Edit template files in `/templates/` directory
- Add more FAQ items in `faq.html`
- Add more loan products in `loan_products.html`