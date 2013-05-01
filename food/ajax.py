from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register

@dajaxice_register
def get_items_list(request, option):
    import pdb
    pdb.set_trace()
    dajax = Dajax()
    option
    restaurant_obj =  Restaurant.objects.get(id=int(option))
    items = restaurant_obj.fooditems
    out = []
    for item in items:
    	out.append("<label class='checkbox'><input type='checkbox' name='item_name' id='item_name' value={}>".format(item))
    dajax.assign('#food_items', 'innerHTML', ''.join(out))
    return dajax.json()