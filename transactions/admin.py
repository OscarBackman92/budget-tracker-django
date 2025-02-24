from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "amount", "transaction_type", "category", "date")  # ✅ Display columns
    list_filter = ("transaction_type", "category", "date")  # ✅ Filter options
    search_fields = ("title", "category", "user__username")  # ✅ Search bar
    ordering = ("-date",)  # ✅ Sort by newest transactions

    # ✅ Make it readonly to avoid manual modification of some fields
    readonly_fields = ("date",)

# ✅ Now, the Transactions will be better displayed in the Django Admin panel!
