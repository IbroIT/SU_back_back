# About Section & Partners Backend API

## Overview

The `about_section` Django app provides backend functionality for the Partners component and about section content management. It supports multilingual content (Russian, English, Kyrgyz) and provides optimized API endpoints for the frontend.

## Models

### Partner Model
Manages university partners with the following fields:
- **Basic Info**: name (with translations), icon, logo, website, description
- **Styling**: color_theme, glow_effect (Tailwind CSS classes)
- **Management**: is_active, order, created_at, updated_at

### AboutSection Model
Manages about section content:
- **Content**: title, subtitle, content (with translations)
- **Settings**: is_active, show_partners, partners_animation_speed

## API Endpoints

### Base URL: `/api/about-section/`

### Partners Endpoints

#### 1. Get Partners List
```
GET /api/about-section/partners/
```
Standard REST API endpoint with filtering and search capabilities.

**Query Parameters:**
- `lang`: Language (ru, en, ky)
- `is_active`: Filter by active status
- `color_theme`: Filter by color theme
- `search`: Search in name and description
- `ordering`: Order by fields (order, name, created_at)

#### 2. Get Partner Detail
```
GET /api/about-section/partners/{id}/
```
Get detailed information about a specific partner.

#### 3. Partners for Frontend (Optimized)
```
GET /api/about-section/partners/frontend/
```
Optimized endpoint matching the frontend component data structure.

**Response Format:**
```json
{
  "success": true,
  "count": 8,
  "data": [
    {
      "id": 1,
      "nameKey": "partners.national_hospital",
      "icon": "🏥",
      "color": "from-blue-500 to-indigo-600",
      "glow": "hover:shadow-blue-500/50",
      "name": "National Hospital",
      "description": "Leading medical organization",
      "website": "https://example.com",
      "logo": "/media/partners/logo.png",
      "order": 1
    }
  ]
}
```

#### 4. Partners Statistics
```
GET /api/about-section/partners/stats/
```
Get statistics about partners count.

### About Section Endpoints

#### 1. Get About Sections List
```
GET /api/about-section/about-sections/
```

#### 2. Get About Section Detail
```
GET /api/about-section/about-sections/{id}/
```

#### 3. Get About Section with Partners
```
GET /api/about-section/about-sections/{id}/with-partners/
```

#### 4. Combined Endpoint (Optimized for Frontend)
```
GET /api/about-section/about-with-partners/
```
Gets the main about section with all active partners in one request.

**Response Format:**
```json
{
  "success": true,
  "about_section": {
    "id": 1,
    "title": "Our Partners",
    "subtitle": "We collaborate with leading organizations",
    "content": "Detailed content...",
    "show_partners": true,
    "partners_animation_speed": 0.5
  },
  "partners": [...],
  "partners_count": 8
}
```

## Language Support

All endpoints support multilingual content through:

1. **Query Parameter**: `?lang=en`
2. **HTTP Header**: `Accept-Language: en`
3. **Default**: Russian (ru)

Supported languages:
- `ru` - Russian (default)
- `en` - English  
- `ky` - Kyrgyz

## Frontend Integration

### Updating the React Component

To integrate with the backend, update your Partners component:

```jsx
import { useState, useEffect } from 'react';
import { useTranslation } from 'react-i18next';

const Partners = () => {
  const { i18n } = useTranslation();
  const [partners, setPartners] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchPartners();
  }, [i18n.language]);

  const fetchPartners = async () => {
    try {
      setLoading(true);
      const response = await fetch(
        `http://localhost:8000/api/about-section/partners/frontend/?lang=${i18n.language}`
      );
      const data = await response.json();
      
      if (data.success) {
        setPartners(data.data);
      }
    } catch (error) {
      console.error('Error fetching partners:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div>Loading partners...</div>;
  }

  // Use partners state instead of hardcoded data
  const duplicatedPartners = [...partners, ...partners];

  // Rest of your component logic remains the same
};
```

### Alternative: Combined Endpoint

For better performance, use the combined endpoint:

```jsx
useEffect(() => {
  const fetchData = async () => {
    try {
      const response = await fetch(
        `http://localhost:8000/api/about-section/about-with-partners/?lang=${i18n.language}`
      );
      const data = await response.json();
      
      if (data.success) {
        setPartners(data.partners);
        // Also use data.about_section for section content
      }
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  fetchData();
}, [i18n.language]);
```

## Admin Interface

Access the Django admin at `/admin/` to manage:
- **Partners**: Add, edit, delete partners with multilingual support
- **About Sections**: Manage section content and settings

### Admin Features:
- Color preview for partner themes
- Icon display in list view
- Bulk actions for activation/deactivation
- Search and filtering
- Multilingual field support

## Management Commands

### Populate Initial Data
```bash
python manage.py populate_partners
```
Creates initial partners and about section based on the original frontend data.

## Database Migration

If you need to apply the migrations:
```bash
python manage.py makemigrations about_section
python manage.py migrate
```

## File Structure

```
about_section/
├── __init__.py
├── admin.py              # Django admin configuration
├── apps.py              # App configuration
├── models.py            # Partner and AboutSection models
├── serializers.py       # DRF serializers
├── views.py            # API views
├── urls.py             # URL routing
├── management/
│   └── commands/
│       └── populate_partners.py
└── migrations/
    └── 0001_initial.py
```

## Testing

Test the API endpoints:
```bash
# Test partners
curl "http://localhost:8000/api/about-section/partners/frontend/"

# Test with language
curl "http://localhost:8000/api/about-section/partners/frontend/?lang=en"

# Test combined endpoint
curl "http://localhost:8000/api/about-section/about-with-partners/"
```

## Next Steps

1. **Update Frontend**: Replace hardcoded data with API calls
2. **Add Images**: Upload partner logos through admin
3. **Configure Translation**: Set up proper translation keys
4. **Caching**: Add caching for better performance
5. **Testing**: Add unit tests for models and views

The backend is now ready and provides all the functionality needed for the Partners component with multilingual support and easy content management through Django admin.
