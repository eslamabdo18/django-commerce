from account.models import User, Customer


class CustomerService:

    @staticmethod
    def create_or_update_customer(user: User, guest_id=None):
        if not guest_id:
            return Customer.objects.create(user=user)

        customer = Customer.objects.get(_id=guest_id)
        customer.user = user
        return customer.save()

    @staticmethod
    def create_guest_user():
        guest = Customer.objects.create()
        return guest
