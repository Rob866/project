# Generated by Django 3.2.12 on 2022-02-23 22:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0002_course_grade_level"),
        ("students", "0003_alter_enrollment_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Coursework",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "complete_date",
                    models.DateField(verbose_name="fecha de finalización"),
                ),
                (
                    "course_task",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="courses.coursetask",
                        verbose_name="tarea del curso",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="students.student",
                        verbose_name="estudiante",
                    ),
                ),
            ],
            options={
                "verbose_name": "Trabajo del Curso",
                "verbose_name_plural": "Trabajos del curso",
            },
        ),
    ]
