from flask_restful import Resource, reqparse
from flask import jsonify
from models import InvoiceModel


class Invoice(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('customer_name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('customer_address',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('customer_email',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('customer_number',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('description',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('sl_no',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('quantity',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('rate',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def get(self, invoice_number):
        invoice = InvoiceModel.find_by_number(invoice_number).json()
        shop_details = {"name": "ABC Electronics", "address": "No: 1, XXX Road, YYY, ZZZ-000000",
                        "email": "abcelectronics@xyz.com", "number": "9000000000"}
        if invoice:
            return jsonify([shop_details, invoice])
        return {'message': 'The Invoice number you entered does not exist'}, 404

    def post(self):
        data = Invoice.parser.parse_args()
        item = InvoiceModel(**data)

        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return item.json(), 201