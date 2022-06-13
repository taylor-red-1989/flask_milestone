from db import db
from datetime import datetime


class InvoiceModel(db.Model):

    __tablename__ = 'invoices'
    invoice_number = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(80))
    customer_address = db.Column(db.String(80))
    customer_email = db.Column(db.String(80))
    customer_number = db.Column(db.Integer)
    sl_no = db.Column(db.Integer)
    description = db.Column(db.String(80))
    date = db.Column(db.String(80))
    quantity = db.Column(db.Integer)
    rate = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    sub_total = db.Column(db.Integer)
    discount = db.Column(db.Integer)
    tax = db.Column(db.Integer)
    total = db.Column(db.Integer)

    def __init__(self, customer_name, customer_address, customer_email,
                 customer_number, sl_no, description, quantity, rate):
        self.customer_name = customer_name
        self.customer_address = customer_address
        self.customer_email = customer_email
        self.customer_number = customer_number
        self.sl_no = sl_no
        self.description = description
        self.date = datetime.now().strftime("%d/%m/%Y")
        self.quantity = quantity
        self.rate = rate
        self.amount = self.quantity * self.rate
        self.sub_total = self.amount
        self.discount = 0.05 * self.sub_total
        self.tax = 0.18 * self.discount
        self.total = self.sub_total + self.discount + self.tax

    def json(self):
        invoice_details = {'amount': self.amount, 'customer_address': self.customer_address,
                           'customer_email': self.customer_email, 'customer_name': self.customer_name,
                           'customer_number': self.customer_number, 'date': self.date, 'description': self.description,
                           'discount': self.discount, 'invoice_number': self.invoice_number, 'quantity': self.quantity,
                           'rate': self.rate, 'sl_no': self.sl_no, 'sub_total': self.sub_total, 'tax': self.tax,
                           'total': self.total}
        return invoice_details

    @classmethod
    def find_by_number(cls, invoice_number):
        return cls.query.filter_by(invoice_number=invoice_number).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
