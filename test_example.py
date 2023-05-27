from typing import Any, AsyncGenerator, Generator

from typing_extensions import Literal

from fastapi_inferring_depends import Depends

# type of defined_by_annotation is Any
defined_by_annotation = Depends()


def func_dependency() -> Literal[1]:
    return 1


# type of func_depends is Literal[1] with type inference, Any without
func_depends = Depends(func_dependency)

# explicit assignment for testing with mypy
func_depends_test: Literal[1] = func_depends


def generator_dependency() -> Generator[Literal[1], None, None]:
    yield 1


# type of generator_depends is Literal[1] with type inference, Any without
generator_depends = Depends(generator_dependency)

# explicit assignment for testing with mypy
generator_depends_test: Literal[1] = generator_depends


async def coroutine_dependency() -> Literal[1]:
    return 1


# type of coroutine_depends is Literal[1] with type inference, Any without
coroutine_depends = Depends(coroutine_dependency)

# explicit assignment for testing with mypy
coroutine_depends_test: Literal[1] = coroutine_depends


async def async_generator_dependency() -> AsyncGenerator[Literal[1], None]:
    yield 1


# type of async_generator_depends is Literal[1] with type inference, Any without
async_generator_depends = Depends(async_generator_dependency)

# explicit assignment for testing with mypy
async_generator_depends_test: Literal[1] = async_generator_depends


class CallableClassDependency:
    def __call__(self, *args: Any, **kwds: Any) -> Literal[1]:
        return 1


# type of class_depends is CallableClassDependency with type inference, Any without
class_depends = Depends(CallableClassDependency)

# explicit assignment for testing with mypy
class_depends_test: CallableClassDependency = class_depends

# type of class_depends is Literal[1] with type inference, Any without
callable_object_depends = Depends(CallableClassDependency())

# explicit assignment for testing with mypy
callable_object_depends_test: Literal[1] = callable_object_depends


def func_factory_dependency():
    def _func_dependency() -> Literal[1]:
        return 1

    return _func_dependency


# type of func_factory_depends is Literal[1] with type inference, Any without
func_factory_depends = Depends(func_factory_dependency())

# explicit assignment for testing with mypy
func_factory_depends_test: Literal[1] = func_factory_depends


def generator_factory_dependency():
    def _generator_dependency() -> Generator[Literal[1], None, None]:
        yield 1

    return _generator_dependency


# type of generator_factory_depends Literal[1] with type inference, Any without
generator_factory_depends = Depends(generator_factory_dependency())

# explicit assignment for testing with mypy
generator_factory_depends_test: Literal[1] = generator_factory_depends


def coroutine_factory_dependency():
    async def _coroutine_dependency() -> Literal[1]:
        return 1

    return _coroutine_dependency


# type of coroutine_factory_depends is Literal[1] with type inference, Any without
coroutine_factory_depends = Depends(coroutine_factory_dependency())

# explicit assignment for testing with mypy
coroutine_factory_depends_test: Literal[1] = coroutine_factory_depends


def async_generator_factory_dependency():
    async def _async_generator_dependency() -> AsyncGenerator[Literal[1], Any]:
        yield 1

    return _async_generator_dependency


# type of async_generator_factory_depends is Literal[1] with type inference, Any without
async_generator_factory_depends = Depends(async_generator_factory_dependency())


# explicit assignment for testing with mypy
async_generator_factory_depends_test: Literal[1] = async_generator_factory_depends
