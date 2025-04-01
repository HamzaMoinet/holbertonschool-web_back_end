export default function getStudentIDsSum(students) {
  return students.reduce((sum, students) => sum + students.id, 0);
}
