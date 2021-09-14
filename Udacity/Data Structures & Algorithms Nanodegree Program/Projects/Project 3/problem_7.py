from typing import List

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler: str, not_found_handler: str):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()
        self.root.handler = root_handler
        self.not_found_handler = not_found_handler

    def insert(self, route_list: List[str], handler: str = None):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root
        for i in range(len(route_list) - 1):
            node = node.insert(route_list[i])

        node.insert(route_list[-1], handler)

    def find(self, route_list: List[str]) -> str:
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root
        for route in route_list:
            if node is None:
                break
            node = node.children.get(route)

        if node is None or node.handler is None:
            return self.not_found_handler

        return node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.route = None
        self.handler = None

    def insert(self, route: str, handler: str = None):
        if route not in self.children:
          self.children[route] = RouteTrieNode()

        if handler is not None:
          self.children[route].handler = handler

        return self.children[route]

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler: str, not_found_handler: str):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root_route = RouteTrie(root_handler, not_found_handler)

    def add_handler(self, route: str, handler: str):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        route_list = self.split_path(route)
        self.root_route.insert(route_list, handler)

    def lookup(self, route: str) -> str:
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        route_list = self.split_path(route)
        handler = self.root_route.find(route_list)

        return handler

    def split_path(self, route: str) -> list:
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return list(filter(lambda x: x != '', route.split('/')))

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
assert router.lookup("/") == 'root handler'
assert router.lookup("/home") == 'not found handler'
assert router.lookup("/home/about") == 'about handler'
assert router.lookup("/home/about/") == 'about handler'
assert router.lookup("/home/about/me") == 'not found handler' 
