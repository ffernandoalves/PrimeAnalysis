#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <cmath>
#include <iostream>
#include <time.h>


static PyObject* prime_residue(PyObject *self, PyObject *args) {
    PyObject *primos;
    PyObject *restos;
    Py_ssize_t i, n;

    if (!PyArg_ParseTuple(args, "O!", &PyList_Type, &primos)) {
        return nullptr;
    }

    n = PyList_Size(primos);
    restos = PyList_New(n);
    if (!restos) {
        return nullptr;
    }
    
    int c = 0;
    for (i = 0; i < n; i++) {
        PyObject *p = PyList_GetItem(primos, i);
        long valor = PyLong_AsLong(p);

        if (valor < 5) {
            PyList_SET_ITEM(restos, i, p);
            c = 0;
        } else {
            long r = valor - (3*c);
            PyObject *r_obj = PyLong_FromLong(r);

            if (!r_obj) {
                Py_DECREF(restos);
                return nullptr;
            }
            PyList_SET_ITEM(restos, i, r_obj);
        }
        c++;
    }

    return restos;
}

static PyObject *is_prime(PyObject *self, PyObject *args) {
    int num;
    if (PyTuple_Check(args)) {
        if (!PyArg_ParseTuple(args, "i", &num)) {
            return NULL;    
        }
    } else {
        num = PyLong_AsLong(args);
    }

    if (num == 2) { Py_RETURN_TRUE ; } // { return Py_BuildValue("i", num) ; } // 
    else if ((num <= 1) || (num % 2 == 0)) { Py_RETURN_FALSE; }

    int i_sqrt_num = (int)sqrt(num);

    for (int div = 3; div < i_sqrt_num + 1; div+=2) {
        if (num % div == 0) { Py_RETURN_FALSE; }
    }

//    return Py_BuildValue("i", num);
    Py_RETURN_TRUE;
}


static PyObject *run_program(PyObject *self, PyObject *args) {
    int N;

    if (!PyArg_ParseTuple(args, "i", &N)) {
        return nullptr;    
    }

    for (int i = 0; i < N; i++) {
        is_prime(self, PyLong_FromLong(i));
    }
    Py_RETURN_NONE;
}


static PyObject *check_primes(PyObject *self, PyObject *args, PyObject *kwargs) {
    int N;
    const char *keywords[2] = {"N", NULL};
    
    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "|i", const_cast<char **>(keywords), &N)){
        return NULL;
    }

    clock_t start, end;
    start = clock();

    run_program(self, PyLong_FromLong(N));

    end = clock();
    std::cout << "time: " << (end - start) / ((double)CLOCKS_PER_SEC) << std::endl;

    Py_RETURN_NONE;
}



//===================PYTHON_MODULE_DEFINITION==========================
static PyMethodDef calc_primes_methods[] = {
    {"is_prime"    , (PyCFunction)is_prime, METH_VARARGS, NULL},
//    {"run_program" , (PyCFunction)run_program , METH_VARARGS, NULL},
    {"check_primes", (PyCFunction)check_primes, METH_VARARGS | METH_KEYWORDS, NULL},
    {"prime_residue", (PyCFunction)prime_residue, METH_VARARGS,
        PyDoc_STR(
            "Seja \'p\' primo, temos as seguinte equações:\n"
            "\t1. r = p, para todo p < 5\n"
            "\t2. r = p - 3*c, c>=0 para todo p >= 5.\n"
            "para todo r, c, p inteiros.")},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef calc_primes_module = {
    PyModuleDef_HEAD_INIT,
    "calc_primes",          /* m_name     */
    "sem doc",              /* m_doc      */
    -1,                     /* m_size     */
    calc_primes_methods,         /* m_methods  */
    NULL,                   /* m_reload   */
    NULL,                   /* m_traverse */
    NULL,                   /* m_clear    */
    NULL,                   /* m_free     */
};

PyMODINIT_FUNC PyInit_calc_primes(void){
    Py_Initialize();
    return PyModule_Create(&calc_primes_module);
}