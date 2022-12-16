.. SPDX-FileCopyrightText: 2022 Sidings Media <contact@sidingsmedia.com>
.. SPDX-License-Identifier: CC-BY-SA-4.0

Node Communication
==================

Communication between :term:`nodes<node>` is vital to ensure proper
operation of the control system. Due to the distributed nature of the
system, a standardised system to communicate between nodes is essential.
There are two ways in which nodes communicate within the network.
Clients will usually communicate with the :term:`command node` board via the
REST API provided by the client bridge. Nodes will usually communicate
with each other over serial interfaces such as sockets, I2C and UART. In
order to ensure that communication is as smooth as posible, simple
standards for both serial communication and communication with the REST
API have been developed. The API is documented using the OpenAPI 3.1
specification and the serial communication is defined using Augmented
Backus–Naur form (ABNF) as defined by `RFC 5234`_.

Registers
---------

Registers are conceptually similar to pigeonholes. In short, they are
named locations on each node that store specific pieces of configuration
data. These registers can be accessed and modified over the supported
communications protocols. These form the basis for each nodes API and
the registers are used to control the functionality of each node.

Each register has a locally unique address in the following format:

.. code-block:: abnf
    :caption: ABNF specification for a registers address

    register-addr   =       1*(ALPHA / %x2D / %x5F)
                                ; Only support alphanumeric characters as
                                ; well as - and _ 

This address is used by commands to retrieve and modify the data in a
specific register.

.. note::
    Register addresses are case insensitive. I.e. speed_channel_1 is
    the same as SPEED_CHANNEL_1.

In cases where a request is made for the contents of a register but the
register is empty, ``null`` should be returned.


Reserved registers
^^^^^^^^^^^^^^^^^^

A number of addresses are reserved for use and MUST be present on all
nodes. They are used by the control nodes to establish the specific
features that an individual node supports and are essential to the
correct interoperation of all nodes.

.. glossary::

    registers
        A comma seperated list of all supported register addresses
        available on this node. The comma seperated list SHOULD have the
        following format.

        .. code-block:: abnf
            :caption: ABNF specification for register list

            register-list   =       *(register-addr %x4C)
                                        ; 0 or more register addresses
                                        ;   seperated by a comma without
                                        ;   any spaces

        .. note:: 
            Any whitespace will be removed during processing of the list
                                 

    serial
        A 16 character long string representing the serial number of the
        node. The serial number is an arbitary string that MAY be unique
        among boards. It is used solely for informational purposes. If
        no serial number is defined, ``null`` SHOULD be returned.

    model
        The model number of this node. The model number is an arbitary
        string of maximum length 256 characters that does not need to be
        unique. It is used solely for informational purposes. If no
        model number is defined, ``null`` SHOULD be returned.

    bootloader
        A string representing the current bootloader version installed
        on this node. This SHOULD be filled on all nodes. It is used to
        establish compatibility of firmware and supported features.

    firmware
        A string representing the current firmware version installed on
        the node. This SHOULD be filled in on all nodes.

Client to Node
--------------

REST API
^^^^^^^^

This is used as the main form of communication between a :term:`client
bridge` and a :term:`client`. The specification is defined using the
`OpenAPI 3.1 standard`_ and is listed below. A complete list of HTTP
routes is also available at the end of this document. An `interactive
version`_ of the OpenAPI documentation is also available.

.. openapi:: ../specifications/REST-API/openapi.yaml

Bootloader
^^^^^^^^^^

The client may, in order to complete some actions, decide to communicate
with the bootloader interface of a :term:`node`. If this is the case,
the `reset` command should be issued to the board, and then any
character send along the USB interface after approximately 1 second.
This is to interupt the boot process. Various commands may then be sent
to the bootloader as detailed below.

.. literalinclude:: ../specifications/serial/client-node.abnf
    :language: abnf
    :caption: ABNF specification for client to node serial communication

Node to Node
------------

Serial Commands
^^^^^^^^^^^^^^^

Serial commands are used for inter-node communication in almost all
cases. Most nodes are connected via serial communication mediums such as
I2C, UART and sockets. In these cases, the below specification for
serial commands should be used. 

These commands are loosely inspired by SQL statements. There are two
types of command, the ``get`` command and the ``set`` command. As the
names suggest, ``get`` commands retrieve a value from a register and
``set`` commands set the value of a register.

In most cases, it is required to state the address of the node the
command is being sent to. This is to facilitate the command traversing
client bridges and interface cards. The only circumstance where the
address can be omitted is on commands sent by the :term:`command node`
to devices directly connected on the I2C bus. This is possible as the
address is already specified by the :term:`command node` when sending
the command over the I2C bus.

.. literalinclude:: ../specifications/serial/node-node.abnf
    :language: abnf
    :caption: ABNF specification for node to node serial communication


.. _`RFC 5234`: https://www.rfc-editor.org/rfc/rfc5234.html
.. _`interactive version`: https://docs.railwaycontroller.sidingsmedia.com/projects/dev/en/latest/api/clientbridge.html
.. _`OpenAPI 3.1 standard`: https://spec.openapis.org/oas/latest.html
