#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 19:15:12 2023

@author: abdullahalshihry
"""

import qiskit as qs
import qiskit.visualization as qv
import random
import qiskit.circuit as qf






def Deutsch(circuit):
    qr = qs.QuantumRegister(2,'q')
    cr = qs.ClassicalRegister(1,'c')
    qc = qs.QuantumCircuit(qr,cr)
    qc.x(qr[1])
    qc.barrier(range(2))
    qc.h(qr[0])
    qc.h(qr[1])
    qc.barrier(range(2))
    qc = qc.compose(circuit)
    qc.barrier(range(2))
    qc.h(qr[0])
    qc.barrier(range(2))
    qc.measure(0,0)
    job1 = qs.execute(qc, qs.Aer.get_backend('aer_simulator'), shots = 1024)
    output1 = job1.result().get_counts()
    print(output1)
    qc.draw('mpl')
    

def Oracle():
    qr = qs.QuantumRegister(2,'q')
    cr = qs.ClassicalRegister(1,'c')
    qc = qs.QuantumCircuit(qr,cr)
    qq = qs.QuantumCircuit(2,name='Uf')
    
    v = random.randint(1, 4)
    
    if v == 1:
        qq.i(qr[0])
        qq.i(qr[1])
    elif v == 2:
        qq.i(qr[0])
        qq.x(qr[1])
    elif v == 3:
        qq.cx(0,1)
    elif v == 4:
        qq.cx(0,1)
        qq.x(1)
    
    qq =qq.to_gate()
    qc.append(qq,[0,1])
    return qc
    

    
Deutsch(Oracle())

