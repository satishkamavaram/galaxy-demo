#! /usr/bin/env python3
DOCUMENTATION = """
module: inventory
short_description: Inventory list
description: This inventory module
notes: 
- Tested against 20.4.1.1
options: 
  regex:
    description:
    - Regular expression matching device name, type or model to display
    required: false
    type: str
  not_regex:
    description:
    - Regular expression matching device name, type or model NOT to display.
    required: false
    type: str
  reachable:
    description:
    - Display only reachable devices
    required: false
    type: bool
    default: False
"""

EXAMPLES = """
- name: Get inventory devices
  satish.custom.inventory:
    regex: ".*"
    reachable: true
"""

RETURN = """
stdout:
  description: Status of inventory 
  returned: always apart from low level errors
  type: str
  sample: 'Task inventory completed successfully'
stdout_lines:
  description: The value of stdout split into a list
  returned: always apart from low level errors
  type: list
  sample: show table view data
"""
from ansible.module_utils.basic import AnsibleModule
from pydantic import ValidationError

def main():
    module_args = dict(
        regex=dict(type="str"),
        not_regex=dict(type="str"),
        reachable=dict(type="bool"),
    )
    module = AnsibleModule(
        argument_spec=module_args,
        mutually_exclusive=[('regex', 'not_regex')],
        supports_check_mode=True
    )

    try:
   
        result = {
            "changed": False,
            "json": "success"
        }
        module.exit_json(**result)

    except ValidationError as ex:
        module.fail_json(msg=f"Invalid inventory parameter: {ex}")


if __name__ == "__main__":
    main()
