:source: inventory.py

:orphan:

.. _inventory_module:


inventory - Inventory  List
+++++++++++++++++++++++++++++++++


.. contents::
   :local:
   :depth: 2


Synopsis
--------
- This inventory module.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
                        <th width="100%">Comments</th>
        </tr>
                    
                               
                                <tr>
                                                                <td colspan="1">
                    <b>not_regex</b>
                    <br/><div style="font-size: small; color: red">str</div>                                                        </td>
                                <td>
                                                                                                                                                            </td>
                                                                <td>
                                                                        <div>Regular expression matching device name, type or model NOT to display.</div>
                                                                                </td>
            </tr>
                                
                                
                                <tr>
                                                                <td colspan="1">
                    <b>reachable</b>
                    <br/><div style="font-size: small; color: red">bool</div>                                                        </td>
                                <td>
                                                                                                                                                                                                                    <ul><b>Choices:</b>
                                                                                                                                                                <li><div style="color: blue"><b>no</b>&nbsp;&larr;</div></li>
                                                                                                                                                                                                <li>yes</li>
                                                                                    </ul>
                                                                            </td>
                                                                <td>
                                                                        <div>Display only reachable devices</div>
                                                                                </td>
            </tr>
                                
                        </table>
    <br/>


Notes
-----

.. note::
    - Tested against 20.4.1.1


Examples
--------

.. code-block:: yaml+jinja

    
    - name: Get inventory devices
      satish.custom.inventory:
        regex: ".*"
        reachable: true





Status
------




Author
~~~~~~

- UNKNOWN


.. hint::
    If you notice any issues in this documentation you can `edit this document <https://github.com/ansible/ansible/edit/devel/lib/ansible/modules/inventory.py?description=%3C!---%20Your%20description%20here%20--%3E%0A%0A%2Blabel:%20docsite_pr>`_ to improve it.
