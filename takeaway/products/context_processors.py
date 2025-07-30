from .models import Cart

# Marking cart_item_quantity a global variable for layout.html.
def cart_item_quantity(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(
            user=request.user, completed=False)
        return {'cart_item_quantity':cart.num_of_items}
    return{'cart_item_quantity':0}