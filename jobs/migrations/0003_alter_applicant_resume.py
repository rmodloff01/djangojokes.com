# Generated by Django 5.1 on 2024-08-27 18:41

import jobs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_applicant_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='resume',
            field=models.FileField(blank=True, help_text='PDFs only', upload_to='private/resumes', validators=[jobs.models.validate_pdf]),
        ),
    ]
