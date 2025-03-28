export default function createReportObject(employeesList) {
  return {
    allemplyeeslist: { ...employeesList },
    getNumberOfDepartments(employees) {
      return Object.keys(employees).length;
    },
  };
}
