# plp-python-week7: Shopping List Manager

## File Descriptions
- **list_warmup.py**: Demonstrates basic list operations like indexing, appending, removing, and checking length.
- **shopping_list.py**: An interactive menu-driven program to add, remove, and show items safely.
- **list_report.py**: Analyzes a preset list of items to provide a numbered report, counts items with >4 letters, and determines the longest item name.

## Reflection
**Why is it safer to check `in` before calling `.remove()`?**
Checking membership with the `in` keyword ensures that an item actually exists inside the list before attempting to delete it. If you call `.remove()` on a non-existent item without checking first, Python will raise a `ValueError` crash. Using a conditional check keeps the application running smoothly and allows you to give the user a friendly error message instead.
