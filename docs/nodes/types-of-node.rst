.. SPDX-FileCopyrightText: 2022 Sidings Media <contact@sidingsmedia.com>
.. SPDX-License-Identifier: CC-BY-SA-4.0

Types of node
=============

There are two main classes of node withing the railway controller
system, the :term:`command node` and :term:`control nodes<control
node>`. Within the :term:`control node` classification, there are
multiple subclasses to indicate the functionality of the node and to
dictate the role it has within the control system.

.. index::
    command node

Command node
------------

The :term:`command node` is the central :term:`node` in the railway
control system. All commands are either generated by, or pass through
the :term:`command node`. It is responsible for making descisions based
upon the client inputs, as well as its knowledge of the current state of
the railway based upon previous commands as well as optional sensors
placed around the network. There MUST only be one control node per
railway control network.

Control node
------------

The :term:`control node` is responsible for directly interfacing with
the railway infrastructure. :term:`Control nodes<control node>` receive
commands from the :term:`command node` and adjusts its output
accordingly. Each railway controller network will contain multiple
:term:`control nodes<control node>` that will control different aspects
of the railway from the speed of the trains, to signals and points to
monitoring position sensors to alert the :term:`command node` when a
:term:`block` is occupied. There are different classes of :term:`control
node`.

Classes of control node
^^^^^^^^^^^^^^^^^^^^^^^

.. glossary::

    Speed control node
        The speed control node is responsible for controlling the speed
        of the trains on the track. Each node can drive one distinct
        line.
        
    Accessory control node
        The accessory control node is responsible for controlling
        accessories such as signals and lighting throughout the layout.

    Isolation control node
        The isolation control node is responsible for controlling the
        isolation sections of the network. It contains a number of
        relays that can be used to supply or cut power to a section of track. 

