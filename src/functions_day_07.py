from anytree import Node


def parse_tree(input_file: str) -> Node:
    """

    Args:
        input_file:

    Returns:

    """
    input_file = open(input_file, 'r')
    lines = input_file.readlines()

    # initialize:
    tree = Node("root")
    current_folder = tree

    # parse tree
    for this_line in lines:
        line = this_line.strip()
        if line == "$ cd /":
            current_folder = tree

        elif line == "$ ls":
            pass

        elif line[0:4] == "dir ":
            _, dir_name = line.split(sep=" ")
            Node(dir_name, parent=current_folder, element_type='dir')

        elif line[0:7] == "$ cd ..":
            current_folder = current_folder.parent

        elif line[0:5] == "$ cd ":
            _, _, subfolder = line.split(sep=" ")
            current_folder = [leaf for leaf in current_folder.children if leaf.name == subfolder][0]

        else:
            file_size, file_name = line.split(sep=" ")
            Node(file_name, parent=current_folder,
                 element_type='file', file_size=int(file_size))

    return tree


def list_folder_sizes(tree: Node) -> list:
    """

    Args:
        tree:

    Returns:

    """
    sizes = [_folder_sizes(tree)]

    for element in tree.descendants:
        if element.element_type == 'file':
            pass
        if element.element_type == 'dir':
            sizes.append(_folder_sizes(element))

    return sizes


def _folder_sizes(tree: Node) -> int:
    """

    Args:
        tree:

    Returns:

    """
    cum_size = 0
    for child in tree.children:
        if child.element_type == 'file':
            cum_size += child.file_size
        if child.element_type == "dir":
            cum_size += _folder_sizes(child)

    return cum_size


def find_cum_size(sizes: list, cut_max: int) -> int:
    """

    Args:
        sizes:
        cut_max:

    Returns:

    """

    cum_sum = 0
    for i in sizes:
        if i > cut_max:
            pass
        else:
            cum_sum += i

    return cum_sum


def find_min_size(sizes: list, total_size: int, need: int) -> int:
    """

    Args:
        sizes:
        total_size:
        need:

    Returns:

    """

    free_space = total_size - max(sizes)
    required = need - free_space
    sorted_sizes = sorted(sizes)

    for i in sorted_sizes:
        if i > required:
            return i
        else:
            pass

    raise ValueError('no value found')
