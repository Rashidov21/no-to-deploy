from django_unicorn.components import UnicornView
from players.models import Player

class FormView(UnicornView):
    name = "Bukayo Saka"
    players = Player.objects.all()
    query = None
    finded_players = None
    
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)  # calling super is required
        # obj = Player.objects.get(name=self.name)
        # self.player = obj
        
    def check_state_selected_items(self, obj_name):
        self.player_name = obj_name
        print(self.player_name)
        
        
    
    def search_player(self,*args):
        # for i in dir(self):print(i)
        # print(dir(self.get))
        # print(self.parent)
        print(args)
        print("".join([x for x in args]))
        self.finded_players = self.players.filter(name__icontains="".join([x for x in args]))
     