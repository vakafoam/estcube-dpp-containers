"use strict";
(function (PLATFORM) {
    PLATFORM[PLATFORM['R'] = 1] = 'R';
    PLATFORM[PLATFORM['SciPy'] = 2] = 'SciPy';
    PLATFORM[PLATFORM['Scilab'] = 3] = 'Scilab';
})(exports.PLATFORM || (exports.PLATFORM = {}));
var PLATFORM = exports.PLATFORM;
exports.URLS = {
    'R': 'http://dpp-broker-r:8262/task',
    //'R': 'http://localhost:5000/task',
    'SciPy': 'http://dpp-broker-scipy:8263/task',
    'Scilab': 'http://dpp-broker-scilab:8264/task'
};
//# sourceMappingURL=constants.js.map