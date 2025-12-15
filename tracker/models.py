from django.db import models

class Language(models.Model):

    CATEGORY_CHOICES = [
        ('FSD', 'Full Stack Development'),
        ('CS', 'Cyber Security'),
        ('DS', 'Data Science'),
    ]
    
    
    PROFICIENCY_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Expert', 'Expert'),
    ]
    
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES)
    proficiency = models.CharField(max_length=20, choices=PROFICIENCY_CHOICES, default='Beginner')
    description = models.TextField(blank=True)
    resources = models.TextField(blank=True, help_text="Learning resources or notes")
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"
