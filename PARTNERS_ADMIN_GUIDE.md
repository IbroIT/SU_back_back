# Quick Management Guide - Partners Section

## Admin Access

1. **Login to Django Admin**: http://localhost:8000/admin/
2. **Navigate to**: About Section → Partners or About Sections

## Managing Partners

### Adding a New Partner:
1. Go to Admin → About section → Partners → Add Partner
2. Fill required fields:
   - **Name**: Russian name (required)
   - **Name En/Ky**: English/Kyrgyz translations
   - **Icon**: Emoji (🏥, 🌐, ➕, etc.)
   - **Color theme**: Select from dropdown
   - **Glow effect**: Matching glow color
   - **Order**: Number for display order (0 = first)

3. Optional fields:
   - **Logo**: Upload image (recommended size: 64x64px)
   - **Website**: Partner's official website
   - **Description**: Brief description in all languages

### Editing Partners:
- Click on partner name in admin list
- Modify any field
- Save changes (updates appear immediately on frontend)

### Managing Display:
- **Order**: Lower numbers appear first (0, 1, 2, ...)
- **Active**: Uncheck to hide partner from website
- **Bulk Actions**: Select multiple partners → Actions → "Mark as inactive"

## Managing About Section

### Editing Content:
1. Go to Admin → About section → About sections
2. Click on existing section or add new
3. Update:
   - **Title**: Main heading
   - **Subtitle**: Secondary text
   - **Content**: Detailed description
   - **Show partners**: Enable/disable partners display
   - **Animation speed**: Control scrolling speed (0.1-10.0)

## Color Themes Available:

- `from-blue-500 to-indigo-600` - Blue gradient
- `from-purple-500 to-pink-600` - Purple gradient
- `from-green-500 to-teal-600` - Green gradient
- `from-amber-500 to-orange-600` - Orange gradient
- `from-red-500 to-rose-600` - Red gradient
- `from-indigo-500 to-blue-600` - Indigo gradient
- `from-pink-500 to-rose-600` - Pink gradient
- `from-teal-500 to-emerald-600` - Teal gradient

## Common Tasks:

### Add a new medical partner:
1. Choose appropriate icon (🏥 for hospitals, 🔬 for research, etc.)
2. Set color theme that fits your design
3. Add website URL if available
4. Set order number (typically highest number + 1)

### Change partner display order:
1. Edit each partner's "Order" field
2. Lower numbers appear first in the carousel

### Hide a partner temporarily:
1. Edit partner → Uncheck "Active" → Save
2. Partner disappears from website but data is preserved

### Update section title/content:
1. Edit About Section → Change title/subtitle/content
2. Changes appear immediately on website

## Tips:

- **Icons**: Use medical/professional emojis for better visual appeal
- **Colors**: Try to use different colors for variety
- **Order**: Leave gaps (0, 10, 20, 30) to easily insert new partners later
- **Descriptions**: Keep brief but informative
- **Logos**: 64x64px PNG/JPG work best, transparent backgrounds preferred

## API Endpoints for Developers:

- **All Partners**: `GET /api/about-section/partners/frontend/`
- **With Language**: `GET /api/about-section/partners/frontend/?lang=en`
- **Combined Data**: `GET /api/about-section/about-with-partners/`
- **Single Partner**: `GET /api/about-section/partners/{id}/`

## Frontend Integration:

The React component automatically:
- Fetches fresh data on page load
- Updates when language changes
- Shows loading spinner during fetch
- Falls back to default data if API unavailable
- Handles errors gracefully
