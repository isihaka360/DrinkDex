from .serializer import DrinkSerializer
from .models import Drink
from rest_framework.generics import CreateAPIView , UpdateAPIView , DestroyAPIView ,RetrieveAPIView 

# Here is class based APIviews for serializing and deserializing Drinks,
# in terms of CRUD methods,creating drinks in database , viewing them ,updating them and deleting them

# APIview for viewing Drinks
class DrinkListView(RetrieveAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    lookup_field = '_all_'

# APIview for Adding Drinks in ListView
class AddingDrinkView(CreateAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
  
# APIview for updating Drinks in ListView
class UpdateDrinkView(UpdateAPIView):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    lookup_field = 'pk'
    
# APIview for deleting/removing drinks in Listview 
# Here We do not want to use serializer_class because we delete objects from database directly,
# no needs of serializing them or deserializing them
class DeleteDrinkView(DestroyAPIView):
    queryset = Drink.objects.all()  
    lookup_field = 'pk'  
