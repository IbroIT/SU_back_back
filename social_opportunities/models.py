from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class Event(models.Model):
    """Model for university events"""
    
    CATEGORY_CHOICES = [
        ('events', 'Events'),
        ('forum', 'Forum'),
        ('conference', 'Conference'),
        ('career', 'Career'),
        ('workshop', 'Workshop'),
        ('competition', 'Competition'),
        ('ceremony', 'Ceremony'),
    ]
    
    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    REGISTRATION_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('full', 'Full'),
    ]
    
    COLOR_CHOICES = [
        ('bg-blue-500', 'Blue'),
        ('bg-green-500', 'Green'),
        ('bg-purple-500', 'Purple'),
        ('bg-red-500', 'Red'),
        ('bg-indigo-500', 'Indigo'),
        ('bg-pink-500', 'Pink'),
        ('bg-teal-500', 'Teal'),
        ('bg-amber-500', 'Amber'),
    ]
    
    # Basic fields
    title = models.CharField(
        max_length=200,
        verbose_name='Event Title',
        help_text='Event title in Russian'
    )
    
    title_en = models.CharField(
        max_length=200,
        verbose_name='Event Title (English)',
        help_text='Event title in English',
        blank=True
    )
    
    title_ky = models.CharField(
        max_length=200,
        verbose_name='Иш-чаранын аталышы (Кыргызча)',
        help_text='Event title in Kyrgyz',
        blank=True
    )
    
    description = models.TextField(
        verbose_name='Description',
        help_text='Event description in Russian'
    )
    
    description_en = models.TextField(
        verbose_name='Description (English)',
        help_text='Event description in English',
        blank=True
    )
    
    description_ky = models.TextField(
        verbose_name='Сүрөттөмө (Кыргызча)',
        help_text='Event description in Kyrgyz',
        blank=True
    )
    
    # Event details
    date = models.DateTimeField(
        verbose_name='Event Date',
        help_text='When the event takes place'
    )
    
    location = models.CharField(
        max_length=200,
        verbose_name='Location',
        help_text='Where the event takes place'
    )
    
    location_en = models.CharField(
        max_length=200,
        verbose_name='Location (English)',
        blank=True
    )
    
    location_ky = models.CharField(
        max_length=200,
        verbose_name='Жер (Кыргызча)',
        blank=True
    )
    
    organizer = models.CharField(
        max_length=200,
        verbose_name='Organizer',
        help_text='Who organizes the event'
    )
    
    organizer_en = models.CharField(
        max_length=200,
        verbose_name='Organizer (English)',
        blank=True
    )
    
    organizer_ky = models.CharField(
        max_length=200,
        verbose_name='Уюштуруучу (Кыргызча)',
        blank=True
    )
    
    participants = models.CharField(
        max_length=100,
        verbose_name='Participants Count',
        help_text='Expected number of participants (e.g., "150+", "50-100")',
        blank=True
    )
    
    # Metadata
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='events',
        verbose_name='Category'
    )
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='upcoming',
        verbose_name='Status'
    )
    
    registration = models.CharField(
        max_length=20,
        choices=REGISTRATION_CHOICES,
        default='open',
        verbose_name='Registration Status'
    )
    
    image = models.CharField(
        max_length=10,
        default='📅',
        verbose_name='Icon',
        help_text='Emoji icon for the event'
    )
    
    color = models.CharField(
        max_length=50,
        choices=COLOR_CHOICES,
        default='bg-blue-500',
        verbose_name='Color Theme'
    )
    
    popular = models.BooleanField(
        default=False,
        verbose_name='Popular Event',
        help_text='Mark as popular to show special badge'
    )
    
    social_media_link = models.URLField(
        max_length=500,
        verbose_name='Social Media Link',
        help_text='Link to event social media page (Telegram, Instagram, etc.)',
        blank=True,
        null=True
    )
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ['date']
    
    def __str__(self):
        return self.title


class Club(models.Model):
    """Model for student clubs"""
    
    CATEGORY_CHOICES = [
        ('clubs', 'General'),
        ('academic', 'Academic'),
        ('sports', 'Sports'),
        ('cultural', 'Cultural'),
        ('social', 'Social'),
        ('professional', 'Professional'),
        ('hobby', 'Hobby'),
    ]
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('recruiting', 'Recruiting'),
        ('paused', 'Paused'),
        ('inactive', 'Inactive'),
    ]
    
    COLOR_CHOICES = [
        ('bg-green-500', 'Green'),
        ('bg-blue-500', 'Blue'),
        ('bg-purple-500', 'Purple'),
        ('bg-red-500', 'Red'),
        ('bg-indigo-500', 'Indigo'),
        ('bg-pink-500', 'Pink'),
        ('bg-teal-500', 'Teal'),
        ('bg-amber-500', 'Amber'),
    ]
    
    # Basic fields
    title = models.CharField(
        max_length=200,
        verbose_name='Club Name',
        help_text='Club name in Russian'
    )
    
    title_en = models.CharField(
        max_length=200,
        verbose_name='Club Name (English)',
        help_text='Club name in English',
        blank=True
    )
    
    title_ky = models.CharField(
        max_length=200,
        verbose_name='Клубдун аты (Кыргызча)',
        help_text='Club name in Kyrgyz',
        blank=True
    )
    
    description = models.TextField(
        verbose_name='Description',
        help_text='Club description in Russian'
    )
    
    description_en = models.TextField(
        verbose_name='Description (English)',
        help_text='Club description in English',
        blank=True
    )
    
    description_ky = models.TextField(
        verbose_name='Сүрөттөмө (Кыргызча)',
        help_text='Club description in Kyrgyz',
        blank=True
    )
    
    # Club details
    members = models.CharField(
        max_length=50,
        verbose_name='Members Count',
        help_text='Number of members (e.g., "50+", "25")',
        default='0'
    )
    
    meetings = models.CharField(
        max_length=200,
        verbose_name='Meeting Schedule',
        help_text='When the club meets'
    )
    
    meetings_en = models.CharField(
        max_length=200,
        verbose_name='Meeting Schedule (English)',
        blank=True
    )
    
    meetings_ky = models.CharField(
        max_length=200,
        verbose_name='Жолугушуу графиги (Кыргызча)',
        blank=True
    )
    
    leader = models.CharField(
        max_length=200,
        verbose_name='Club Leader',
        help_text='Name of the club leader'
    )
    
    leader_en = models.CharField(
        max_length=200,
        verbose_name='Club Leader (English)',
        blank=True
    )
    
    leader_ky = models.CharField(
        max_length=200,
        verbose_name='Клуб жетекчиси (Кыргызча)',
        blank=True
    )
    
    achievements = models.JSONField(
        default=list,
        verbose_name='Achievements',
        help_text='List of club achievements in Russian'
    )
    
    achievements_en = models.JSONField(
        default=list,
        verbose_name='Achievements (English)',
        help_text='List of club achievements in English'
    )
    
    achievements_ky = models.JSONField(
        default=list,
        verbose_name='Жетишкендиктер (Кыргызча)',
        help_text='List of club achievements in Kyrgyz'
    )
    
    # Metadata
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='clubs',
        verbose_name='Category'
    )
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active',
        verbose_name='Status'
    )
    
    image = models.CharField(
        max_length=10,
        default='👥',
        verbose_name='Icon',
        help_text='Emoji icon for the club'
    )
    
    color = models.CharField(
        max_length=50,
        choices=COLOR_CHOICES,
        default='bg-green-500',
        verbose_name='Color Theme'
    )
    
    popular = models.BooleanField(
        default=False,
        verbose_name='Popular Club',
        help_text='Mark as popular to show special badge'
    )
    
    social_media_link = models.URLField(
        max_length=500,
        verbose_name='Social Media Link',
        help_text='Link to club social media page (Telegram, Instagram, etc.)',
        blank=True,
        null=True
    )
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Club'
        verbose_name_plural = 'Clubs'
        ordering = ['title']
    
    def __str__(self):
        return self.title


class Project(models.Model):
    """Model for student projects"""
    
    CATEGORY_CHOICES = [
        ('projects', 'General'),
        ('research', 'Research'),
        ('innovation', 'Innovation'),
        ('social', 'Social'),
        ('technology', 'Technology'),
        ('medical', 'Medical'),
        ('environmental', 'Environmental'),
        ('business', 'Business'),
    ]
    
    STATUS_CHOICES = [
        ('planning', 'Planning'),
        ('active', 'Active'),
        ('paused', 'Paused'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    COLOR_CHOICES = [
        ('bg-purple-500', 'Purple'),
        ('bg-blue-500', 'Blue'),
        ('bg-green-500', 'Green'),
        ('bg-red-500', 'Red'),
        ('bg-indigo-500', 'Indigo'),
        ('bg-pink-500', 'Pink'),
        ('bg-teal-500', 'Teal'),
        ('bg-amber-500', 'Amber'),
    ]
    
    # Basic fields
    title = models.CharField(
        max_length=200,
        verbose_name='Project Title',
        help_text='Project title in Russian'
    )
    
    title_en = models.CharField(
        max_length=200,
        verbose_name='Project Title (English)',
        help_text='Project title in English',
        blank=True
    )
    
    title_ky = models.CharField(
        max_length=200,
        verbose_name='Долбоордун аталышы (Кыргызча)',
        help_text='Project title in Kyrgyz',
        blank=True
    )
    
    description = models.TextField(
        verbose_name='Description',
        help_text='Project description in Russian'
    )
    
    description_en = models.TextField(
        verbose_name='Description (English)',
        help_text='Project description in English',
        blank=True
    )
    
    description_ky = models.TextField(
        verbose_name='Сүрөттөмө (Кыргызча)',
        help_text='Project description in Kyrgyz',
        blank=True
    )
    
    # Project details
    team = models.CharField(
        max_length=50,
        verbose_name='Team Size',
        help_text='Number of team members (e.g., "5", "3-7")',
        default='1'
    )
    
    progress = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        default=0,
        verbose_name='Progress Percentage',
        help_text='Project completion percentage (0-100)'
    )
    
    needs = models.JSONField(
        default=list,
        verbose_name='Requirements',
        help_text='List of skills/resources needed in Russian'
    )
    
    needs_en = models.JSONField(
        default=list,
        verbose_name='Requirements (English)',
        help_text='List of skills/resources needed in English'
    )
    
    needs_ky = models.JSONField(
        default=list,
        verbose_name='Талаптар (Кыргызча)',
        help_text='List of skills/resources needed in Kyrgyz'
    )
    
    # Metadata
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='projects',
        verbose_name='Category'
    )
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='planning',
        verbose_name='Status'
    )
    
    image = models.CharField(
        max_length=10,
        default='🚀',
        verbose_name='Icon',
        help_text='Emoji icon for the project'
    )
    
    color = models.CharField(
        max_length=50,
        choices=COLOR_CHOICES,
        default='bg-purple-500',
        verbose_name='Color Theme'
    )
    
    popular = models.BooleanField(
        default=False,
        verbose_name='Popular Project',
        help_text='Mark as popular to show special badge'
    )
    
    social_media_link = models.URLField(
        max_length=500,
        verbose_name='Social Media Link',
        help_text='Link to project social media page (Telegram, Instagram, etc.)',
        blank=True,
        null=True
    )
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
