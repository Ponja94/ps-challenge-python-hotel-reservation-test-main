
# mon tues, wed, thur, fri, sat, sun
# 16   17    18   19   20   21   22
# 23   24    25   26   27   28   29

#entrada de datas

#data_enter = 'Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)'
#data_enter = 'Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)'
#data_enter = 'Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat)'
#data_enter = 'Regular: 29Mar2009(sun)'
#data_enter = 'Regular: 16Mar2009(mon), 17Mar2009(tues)'
data_enter = 'Rewards: 26Mar2009(thur), 27Mar2009(fri), 28Mar2009(sat), 29Mar2009(sun), 30Mar2009(mon)'
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


#class client
class Client:
    def __init__(self, client_type, days_weekday, days_weekend):
        self.client_type = client_type
        self.days_weekday = days_weekday
        self.day_weekend = days_weekend
        


# classe para verificar quantos dias de semana ou de final de semana
class DaysToCheckIn:
    def __init__(self, data_received):
        self.data_received = data_received
        self.counter_weekend = 0
        self.counter_weekday = 0
    
    #função separa string em info
    def counting_days(self):
        infos_client = self.data_received.replace(',','').replace(':','').split()

        #verifica o tipo de cliente
        client_type = infos_client[0]

        #verificando se é dia de semana ou não
        days_to_check_in = infos_client[1:]
        for i in range(len(days_to_check_in)):

            if days_to_check_in[i].find('sat') != -1 or days_to_check_in[i].find('sun') != -1:
                self.counter_weekend+=1
                print(f"final de semana {self.counter_weekend}")
            else:
                self.counter_weekday+=1
                print(f"dia de semana {self.counter_weekday}")
        
        #return self.counter_weekday, self.counter_weekend

#código rodando

days_in = DaysToCheckIn(data_enter)
days_in.counting_days()

client_days_information = Client(client_type, counter_weekday, counter_weekend)

