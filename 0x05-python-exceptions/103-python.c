#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_list - Print basic information about Python lists
 * @p: PyObject list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyObject *item;

	printf("[*] Python list info\n");

	if (PyList_Check(p))
	{
		size = PyList_Size(p);
		allocated = ((PyListObject *)p)->allocated;

		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %zd\n", allocated);

		for (i = 0; i < size; i++)
		{
			item = PyList_GetItem(p, i);
			printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
		}
	}
	else
	{
		printf("[*] Invalid List Object\n");
	}
}

/**
 * print_python_bytes - Print basic information about Python bytes
 * @p: PyObject bytes
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");


	if (PyBytes_Check(p))
	{
		size = PyBytes_Size(p);
		str = PyBytes_AsString(p);

		printf("  size: %zd\n", size);
		printf("  trying string: %s\n", str);
		printf("  first 10 bytes: ");

		for (i = 0; i < size && i < 10; i++)
		{
			printf("%02x ", (unsigned char)str[i]);
		}
		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}

/**
 * print_python_float - Print basic information about Python float
 * @p: PyObject float
 */
void print_python_float(PyObject *p)
{
	double value;

	printf("[.] float object info\n");

	if (PyFloat_Check(p))
	{
		value = PyFloat_AsDouble(p);
		printf("  value: %f\n", value);
	}
	else
	{
		printf("  [ERROR] Invalid Float Object\n");
	}
}
