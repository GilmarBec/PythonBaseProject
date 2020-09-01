from sample.controller.user import UserController

"""
 * Router must be used to access the routes of your file sys.
 * If used correctly may help you with some routes problems. ;) 
"""


class Router:
    """
     * Controller variables, important to our routes!
    """
    user = UserController()
    
    """
     * Add our Routes here!
    """
    routes = {
        "user.list": user.list_action(),
        "user.new": user.create_action(),
    }

    """
     * Default Route, change this if you want.
    """
    DEFAULT_ROUTE = routes["user.list"]

    """
     * @var string reference: Name of reference on our project.
     *
     * @return function: Function pass by arg. 
    """
    def get(self, reference):
        return self.routes[reference]


# route = Router().DEFAULT_ROUTE
