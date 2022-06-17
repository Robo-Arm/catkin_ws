
"use strict";

let ConfigureControlMode = require('./ConfigureControlMode.js')
let SetSpeedOverride = require('./SetSpeedOverride.js')
let SetEndpointFrame = require('./SetEndpointFrame.js')
let SetPTPCartesianSpeedLimits = require('./SetPTPCartesianSpeedLimits.js')
let SetSmartServoLinSpeedLimits = require('./SetSmartServoLinSpeedLimits.js')
let SetWorkpiece = require('./SetWorkpiece.js')
let SetPTPJointSpeedLimits = require('./SetPTPJointSpeedLimits.js')
let SetSmartServoJointSpeedLimits = require('./SetSmartServoJointSpeedLimits.js')
let TimeToDestination = require('./TimeToDestination.js')

module.exports = {
  ConfigureControlMode: ConfigureControlMode,
  SetSpeedOverride: SetSpeedOverride,
  SetEndpointFrame: SetEndpointFrame,
  SetPTPCartesianSpeedLimits: SetPTPCartesianSpeedLimits,
  SetSmartServoLinSpeedLimits: SetSmartServoLinSpeedLimits,
  SetWorkpiece: SetWorkpiece,
  SetPTPJointSpeedLimits: SetPTPJointSpeedLimits,
  SetSmartServoJointSpeedLimits: SetSmartServoJointSpeedLimits,
  TimeToDestination: TimeToDestination,
};
