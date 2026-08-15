"""
College Tools Package
Provides utilities for marks and attendance.
"""

from .marks import (
    total_marks,
    average_marks,
    calculate_grade,
)

from .attendance import attendance_percentage

__all__ = [
    "total_marks",
    "average_marks",
    "calculate_grade",
    "attendance_percentage",
]