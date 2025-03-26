export default class ClassRoom {
  constructor(name, lenght, students) {
    this.name = name;
    this.lenght = lenght;
    this.students = students;
  }

  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Name must be a string');
    } else {
      this._name = value;
    }
  }

  get lenght() {
    return this._lenght;
  }

  set lenght(len) {
    if (typeof len !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this._lenght = len;
  }

  get students() {
    return this._students;
  }

  set students(array) {
    if (!(array instanceof Array)) {
      throw new TypeError('Students must be an array');
    }
    if (!array.every((student) => typeof student === 'string')) {
      throw new TypeError('Each student must be a string');
    }
    this._students = array;
  }
}
