"""This is a classic Object-Oriented Design (OOD) interview question often sourced from the 
book Cracking the Coding Interview.

1. Problem Statement: Design a Call Center
Objective:
Design a system for a call center that handles incoming calls. 
The call center should have three levels of employees: Operators, Supervisors, and Directors.

Rules and Constraints:

Hierarchy: Incoming calls are first assigned to an available Operator.

Escalation: If an Operator cannot handle the call (or none are free), it escalates to a Supervisor. 
If no Supervisor is free or can handle it, it escalates to a Director.

Capacity: Assume Directors can handle any call.

Queuing: If no employee at any level is available to take a call, the call must be placed in a queue
 and handled as soon as an employee becomes free.

Completion: Once a call is finished, the employee becomes free to take another call from the queue."""


# --- COMPONENTS OVERVIEW ---
# Entities:
# - Call: Represents an incoming call with its state and rank.
# - Employee: Abstract class for employees in the call center.
# - Operator, Supervisor, Director: Concrete classes for different employee levels.

# Controller:
# - CallCenter: Manages call dispatching, employee availability, and call queuing.

# Service:
# - The logic for handling calls and employee interactions is encapsulated within the CallCenter class.

# we will use deque for employee wait time with a timer like the problem in CPU processor waiting time
from abc import ABC, abstractmethod
from collections import deque
from enum import IntEnum, auto
from typing import List, Optional, Deque

# --- 1. ENUMS (Constants) ---
class Rank(IntEnum):
    OPERATOR = 0
    SUPERVISOR = 1
    DIRECTOR = 2

class CallState(IntEnum):
    READY = auto()
    IN_PROGRESS = auto()
    COMPLETE = auto()

# --- 2. THE CALL CLASS ---
class Call:
    def __init__(self, rank: Rank = Rank.OPERATOR):
        self.state: CallState = CallState.READY
        self.rank: Rank = rank
        self.employee: Optional['Employee'] = None

    def __repr__(self):
        return f"Call(Rank: {self.rank.name}, ID: {id(self)})"

# --- 3. THE BASE EMPLOYEE (ABSTRACT CLASS) ---
class Employee(ABC):
    def __init__(self, employee_id: int, name: str, rank: Rank, call_center: 'CallCenter'):
        self.employee_id = employee_id
        self.name = name
        self.rank = rank
        self.current_call: Optional[Call] = None
        self.call_center = call_center

    def take_call(self, call: Call) -> None:
        self.current_call = call
        call.employee = self
        call.state = CallState.IN_PROGRESS
        print(f"  >> [{self.rank.name}] {self.name} is now BUSY with {call}")

    def complete_call(self) -> None:
        if self.current_call:
            print(f"  << [{self.rank.name}] {self.name} COMPLETED {self.current_call}")
            self.current_call.state = CallState.COMPLETE
            self.current_call = None
            # Trigger the call center to check if someone is waiting in the queue
            self.call_center.notify_employee_free(self)

    @abstractmethod
    def escalate_call(self) -> None:
        """Each subclass defines where the call goes next."""
        pass

    def _perform_escalation(self, new_rank: Rank) -> None:
        if self.current_call:
            call = self.current_call
            print(f"  !! [{self.rank.name}] {self.name} is ESCALATING {call} to {new_rank.name}")
            
            call.state = CallState.READY
            call.rank = new_rank
            self.current_call = None
            
            # 1. Try to find someone for the escalated call
            self.call_center.dispatch_call(call)
            # 2. Since this employee is now free, check the queue for themselves
            self.call_center.notify_employee_free(self)

# --- 4. CONCRETE CLASSES (INHERITANCE) ---
class Operator(Employee):
    def __init__(self, employee_id: int, name: str, call_center: 'CallCenter'):
        super().__init__(employee_id, name, Rank.OPERATOR, call_center)

    def escalate_call(self) -> None:
        self._perform_escalation(Rank.SUPERVISOR)

class Supervisor(Employee):
    def __init__(self, employee_id: int, name: str, call_center: 'CallCenter'):
        super().__init__(employee_id, name, Rank.SUPERVISOR, call_center)

    def escalate_call(self) -> None:
        self._perform_escalation(Rank.DIRECTOR)

class Director(Employee):
    def __init__(self, employee_id: int, name: str, call_center: 'CallCenter'):
        super().__init__(employee_id, name, Rank.DIRECTOR, call_center)

    def escalate_call(self) -> None:
        raise NotImplementedError('Directors must be able to handle any call')

# --- 5. THE CONTROLLER (CALL CENTER) ---
class CallCenter:
    def __init__(self, operators: List[Operator], supervisors: List[Supervisor], directors: List[Director]):
        self.employees: List[List[Employee]] = [operators, supervisors, directors]
        self.queued_calls: Deque[Call] = deque()

    def dispatch_call(self, call: Call) -> None:
        """Main entry point for any incoming or escalated call."""
        employee = self._find_available_employee(call.rank)
        
        if employee:
            employee.take_call(call)
        else:
            print(f"  -- No available staff for {call.rank.name}. Adding to Queue.")
            self.queued_calls.append(call)

    def _find_available_employee(self, rank: Rank) -> Optional[Employee]:
        # Search starting from the required rank up to Director
        for r in range(rank, len(self.employees)):
            for employee in self.employees[r]:
                if employee.current_call is None:
                    return employee
        return None

    def notify_employee_free(self, employee: Employee) -> None:
        """Checks if there's a call in the queue this specific employee can handle."""
        if self.queued_calls:
            # For simplicity, the employee takes the first call in the queue
            call = self.queued_calls.popleft()
            print(f"  [Queue] Picking up {call} from queue for {employee.name}")
            employee.take_call(call)

# --- 6. EXAMPLE EXECUTION ---
if __name__ == "__main__":
    # Initialize center with empty lists first
    cc = CallCenter([], [], [])

    # Create staff
    ops = [Operator(1, "Alice", cc), Operator(2, "Bob", cc)]
    sups = [Supervisor(3, "Charlie", cc)]
    dirs = [Director(4, "Diane", cc)]

    # Register staff to center
    cc.employees = [ops, sups, dirs]

    print("--- SIMULATION START ---")

    # 1. First call comes in
    print("\nAction: Call 1 arrives.")
    call1 = Call()
    cc.dispatch_call(call1)

    # 2. Call 1 is too hard, Operator Alice escalates it
    print("\nAction: Alice escalates Call 1.")
    ops[0].escalate_call() 

    # 3. More calls arrive to fill up all staff
    print("\nAction: Filling up remaining staff.")
    cc.dispatch_call(Call()) # Bob takes this
    cc.dispatch_call(Call()) # Charlie is busy with Call 1, so Diane takes this
    cc.dispatch_call(Call()) # Everyone is busy! Should queue.

    # 4. A staff member finishes, should trigger queue
    print("\nAction: Bob finishes his call.")
    ops[1].complete_call() 

    print("\n--- SIMULATION END ---")