from pathlib import Path


def generate_tensorboard_experiment_directory(root: str, parents=True) -> str:
    root = Path(root).resolve()
    child = create_from_missing(root) if not root.exists() else create_from_existing(root)
    child.mkdir(parents=parents)
    return child.as_posix()


def create_from_missing(root):
    return root / '0'


def create_from_existing(root):
    children = [int(c.name) for c in root.glob('*') if (c.is_dir() and c.name.isnumeric())]
    return (
        root / '0'
        if is_first_experiment(children)
        else root / increment_experiment_number(children)
    )


def is_first_experiment(children: list[int]) -> bool:
    return not children


def increment_experiment_number(children: list[int]) -> str:
    return str(max(children) + 1)
