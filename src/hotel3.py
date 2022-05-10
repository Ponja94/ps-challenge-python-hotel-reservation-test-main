
# mon tues, wed, thur, fri, sat, sun
# 16   17    18   19   20   21   22
# 23   24    25   26   27   28   29

#entrada de datas

#data_enter = 'Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)'
#data_enter = 'Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)'
#data_enter = 'Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)'
#data_enter = 'Regular: 29Mar2009(sun)'
#data_enter = 'Regular: 16Mar2009(mon), 17Mar2009(tues)'
data_enter = 'Reward: 16Mar2009(sun), 17Mar2009(tues)'

#data_enter = 'Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat), 29Mar2009(sun), 30Mar2009(mon)'
#data_enter_format = 'client: data1, data2, data3, ...' 



#class hotel
class Hotel:
    def __init__(self, name, rate, tax_regular_weekday, tax_regular_weekend, tax_reward_weekday, tax_reward_weekend):
        self.name = name
        self.rate = rate
        self.tax_regular_weekday = tax_regular_weekday
        self.tax_regular_weekend = tax_regular_weekend
        self.tax_reward_weekday = tax_reward_weekday
        self.tax_reward_weekend = tax_reward_weekend
    

#dados  hotel
hotel_lakewood = Hotel('Lakewood','3','110','80','90','80')
hotel_bridgewood = Hotel('Bridgewood','4','160','110','60','50')
hotel_ridgewood = Hotel('Ridgewood','5','220','100','150','40')




class Client():
    def __init__(self, data_received):
        self.data_received = data_received
        self.counter_weekend = 0
        self.counter_weekday = 0
        self.cost_weekday = 0
        self.cost_weekend = 0
        self.client_type = ''
        self.lakewood_cost = 0
        self.bridgewood_cost = 0
        self.ridgewood_cost = 0
    
    #função separa string em info
    def counting_days(self):
        infos_client = self.data_received.replace(',','').replace(':','').split()

        #verifica o tipo de cliente
        self.client_type = infos_client[0]
        #verificando se é dia de semana ou não
        days_to_check_in = infos_client[1:]
        for i in range(len(days_to_check_in)):
            if days_to_check_in[i].find('sat') != -1 or days_to_check_in[i].find('sun') != -1:
                self.counter_weekend+=1
            
            else:
                self.counter_weekday+=1
        #print(f"tipo: {self.client_type}, dia de semana {self.counter_weekday}, final de semana {self.counter_weekend}")



    def client_cost(self):
        if self.client_type == 'Regular':
            lakewood_weekday = int(hotel_lakewood.tax_regular_weekday) * self.counter_weekday
            lakewood_weekend = int(hotel_lakewood.tax_regular_weekend) * self.counter_weekend
            self.lakewood_cost = lakewood_weekday+lakewood_weekend
            
            bridgewood_weekday = int(hotel_bridgewood.tax_regular_weekday) * self.counter_weekday
            bridgewood_weekend = int(hotel_bridgewood.tax_regular_weekend) * self.counter_weekend
            self.bridgewood_cost = bridgewood_weekday+bridgewood_weekend
            
            ridgewood_weekday = int(hotel_ridgewood.tax_regular_weekday) * self.counter_weekday
            ridgewood_weekend = int(hotel_ridgewood.tax_regular_weekend) * self.counter_weekend
            self.ridgewood_cost = ridgewood_weekday+ridgewood_weekend
            
        else:
            lakewood_weekday = int(hotel_lakewood.tax_reward_weekday) * self.counter_weekday
            lakewood_weekend = int(hotel_lakewood.tax_reward_weekend) * self.counter_weekend
            self.lakewood_cost = lakewood_weekday+lakewood_weekend
            
            bridgewood_weekday = int(hotel_bridgewood.tax_reward_weekday) * self.counter_weekday
            bridgewood_weekend = int(hotel_bridgewood.tax_reward_weekend) * self.counter_weekend
            self.bridgewood_cost = bridgewood_weekday+bridgewood_weekend
            
            ridgewood_weekday = int(hotel_ridgewood.tax_reward_weekday) * self.counter_weekday
            ridgewood_weekend = int(hotel_ridgewood.tax_reward_weekend) * self.counter_weekend
            self.ridgewood_cost = ridgewood_weekday+ridgewood_weekend

        print(f'lakewood: {self.lakewood_cost} bridgewood: {self.bridgewood_cost} ridgewood: {self.ridgewood_cost}')



#código rodando
#instanciando

client = Client(data_enter)
client.counting_days()

client.client_cost()