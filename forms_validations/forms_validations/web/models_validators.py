from django.core.exceptions import ValidationError

from forms_validations.web.models import Todo


def validate_max_todos_per_person(assignee):
    if assignee.todo_set.count() >= Todo.MAX_TODOS_PER_PERSON:
        raise ValidationError(f"{assignee} already has max TODOs assigned.")