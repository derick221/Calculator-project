import datetime as dt

class Record:
    def __init__(self, amount, comment, date):
        self.amount = amount
        self.comment = comment
        if not date:
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today_count = 0
        for record in self.records:
            if record.date == dt.datetime.now().date():
                today_count += record.amount
        return today_count

    def get_week_stats(self):
        week_count = 0
        today = dt.date.today()
        week_ago = today - dt.timedelta(days=7)
        for record in self.records:
            if week_ago <= record.date <= today:
                week_count += record.amount
        return week_count

class CashCalculator(Calculator):
    USD_RATE = 37
    EUR_RATE = 40
    UAH_RATE = 1

    def __init__(self, limit):
        super().__init__(limit)
        self.limit = limit

    def get_today_cash_remained(self, currency):
        currencies = {
            'usd': ('USD', self.USD_RATE),
            'eur': ('EUR', self.EUR_RATE),
            'uah': ('UAH', self.UAH_RATE)
        }

        if currency not in currencies:
            return 'Invalid currency. Get rid of your rubles and enter a valid currency.'

        currency_name, currency_rate = currencies[currency]
        remained_cash = self.limit - self.get_today_stats()
        remained_cash_in_currency = round(remained_cash / currency_rate, 2)

        if remained_cash > 0:
            return f'Today you have {remained_cash_in_currency} {currency_name} left'
        elif remained_cash == 0:
            return 'No money left, hold on'
        else:
            return f'No money left, hold on: your debt is {remained_cash_in_currency} {currency_name}'

class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)
        self.limit = limit

    def get_calories_remained(self):
        remained_calories = self.limit - self.get_today_stats()
        if remained_calories > 0:
            return f'Today you can eat something else, but no more than {remained_calories} kcal'
        else:
            return 'Enough eating!'
