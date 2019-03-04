import ast
from ItemList import item_table
from State import State
import re


escaped_items = {
    "Hookshot" : "Hookshot",
    "Longshot" : "Longshot",
    "Silver_Gauntlets" : "Silver Gauntlets",
    "Golden_Gauntlets" : "Golden Gauntlets",
    "Scarecrow" : "Scarecrow",
    "Distant_Scarecrow" : "Distant Scarecrow"}
for item in item_table:
    escaped_items[re.sub(r'[\'()[\]]', '', item.replace(' ', '_'))] = item

    
def to_c_sym(item:str):
    return item.replace("(","").replace(")","").replace(" ","_").replace("'", "").replace("-","_").upper()

class RuleCAST(ast.NodeTransformer):
    '''Transforms a rule into an AST suitable for C code generation'''

    def __init__(self, world):
        self.world = world


    def visit_Name(self, node):
        if node.id in escaped_items:
            ## gen has() function
            _item = to_c_sym(escaped_items[node.id])
            return ast.Call(
                func=ast.Name(id='has', ctx=ast.Load()),
                args=[ast.Name(id='state', ctx=ast.Load()), ast.Name(id=_item, ctx=ast.Load())],
                keywords=[])

        elif node.id in self.world.__dict__:
            ## gen world option
            return ast.Attribute(
                value=ast.Name(id='option', ctx=ast.Load()),
                attr=node.id,
                ctx=ast.Load())
        elif node.id in State.__dict__:
            ## gen 0 argument state call
            return ast.Call(
                func=ast.Name(id=node.id, ctx=ast.Load()),
                args=[ast.Name(id='state', ctx=ast.Load())],
                keywords=[])
        else:
            return ast.Str(node.id.replace('_', ' '))


    def visit_Tuple(self, node):
        ## gen has function call
        if len(node.elts) != 2:
            raise Exception('Parse Error: Tuple must has 2 values')

        item, count = node.elts

        if isinstance(item, ast.Str):
            item = ast.Name(id=item.s, ctx=ast.Load())

        if not isinstance(item, ast.Name):
            raise Exception('Parse Error: first value must be an item. Got %s' % item.__class__.__name__)

        if not (isinstance(count, ast.Name) or isinstance(count, ast.Num)):
            raise Exception('Parse Error: second value must be a number. Got %s' % item.__class__.__name__)

        if isinstance(count, ast.Name):
            count = ast.Attribute(
                value=ast.Name(id='option', ctx=ast.Load()),
                attr=count.id,
                ctx=ast.Load())

        if item.id in escaped_items:
            item.id = escaped_items[item.id]

        if not item.id in item_table:
            raise Exception('Parse Error: invalid item name')

        return ast.Call(
            func=ast.Name(id='has_c', ctx=ast.Load()),
            args=[  ast.Name(id='state', ctx=ast.Load()),
                    ast.Name(id= to_c_sym(item.id), ctx=ast.Load()), count],
            keywords=[])

    def can_reach(self, node, args):
        reach_dest =  to_c_sym(node.args[0].id)
        loc_type = "REGION"
        if len(node.args) == 2:
            loc_type = to_c_sym(node.args[1].id)

        if len(node.args) == 1:
            reach_dest = "{}_{}".format(loc_type, reach_dest)
            args.append(ast.Name(id=reach_dest, ctx=ast.Load()))
            args.append(ast.Name(id='CAN_REACH_{}'.format(loc_type), ctx=ast.Load()))
            return ast.Call(
                func=ast.Name(id=node.func.id, ctx=ast.Load()),
                args=args,
                keywords=node.keywords)

    def has_projectile(self, node, args):
        age = "AGE_" + to_c_sym(node.args[0].id)
        args.append(ast.Name(id=age, ctx=ast.Load()))
        return ast.Call(
            func=ast.Name(id=node.func.id, ctx=ast.Load()),
            args=args,
            keywords=node.keywords)

    def visit_Call(self, node):
        
        if not isinstance(node.func, ast.Name):
            return node

        _func = node.func.id
        new_args = [ast.Name(id='state', ctx=ast.Load())]
        if _func == "can_reach":
            return self.can_reach(node, new_args)
        if _func == "has_projectile":
            return self.has_projectile(node, new_args)

        for child in node.args:
            if isinstance(child, ast.Name):
                if child.id in self.world.__dict__:
                    child = ast.Attribute(
                        value=ast.Name(id='option', ctx=ast.Load()),
                        attr=child.id,
                        ctx=ast.Load())
                elif child.id in escaped_items:
                    child = ast.Name(id=to_c_sym(escaped_items[child.id]), ctx=ast.Load())
                else:
                    child = ast.Str(child.id.replace('_', ' '))
            new_args.append(child)

        return ast.Call(
            func=ast.Name(id=node.func.id, ctx=ast.Load()),
            args=new_args,
            keywords=node.keywords)


    def visit_Subscript(self, node):
        if isinstance(node.value, ast.Name):
            ## should fix to be more dynamically generated
            slice_val = "TRIAL_" + to_c_sym(node.slice.value.id)
            return ast.Subscript(
                value=ast.Attribute(
                    value=ast.Name(id='option', ctx=ast.Load()),
                    attr=node.value.id,
                    ctx=ast.Load()),
                slice=ast.Index(value=ast.Name(id=slice_val, ctx=ast.Load())),
                ctx=node.ctx)
        else:
            return node


    def visit_Compare(self, node):
        if isinstance(node.left, ast.Name):
            if node.left.id in escaped_items:
                node.left = ast.Str(escaped_items[node.left.id])

        if isinstance(node.comparators[0], ast.Name):
            if node.comparators[0].id in escaped_items:
                node.comparators[0] = ast.Str(escaped_items[node.comparators[0].id])

        self.generic_visit(node)
        return node

