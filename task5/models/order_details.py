from exceptions.incomplete_order_exception import IncompleteOrderException

class OrderDetail:
    def validate(self):
        if not self._product:
            raise IncompleteOrderException("Product is missing in order detail.")
