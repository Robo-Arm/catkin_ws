
"use strict";

let SetPTPCartesianSpeedLimits = require('./SetPTPCartesianSpeedLimits.js')
let SetPTPJointSpeedLimits = require('./SetPTPJointSpeedLimits.js')
let SetWorkpiece = require('./SetWorkpiece.js')
let TimeToDestination = require('./TimeToDestination.js')
let SetSmartServoLinSpeedLimits = require('./SetSmartServoLinSpeedLimits.js')
let SetSpeedOverride = require('./SetSpeedOverride.js')
let SetEndpointFrame = require('./SetEndpointFrame.js')
let ConfigureControlMode = require('./ConfigureControlMode.js')
let SetSmartServoJointSpeedLimits = require('./SetSmartServoJointSpeedLimits.js')

module.exports = {
  SetPTPCartesianSpeedLimits: SetPTPCartesianSpeedLimits,
  SetPTPJointSpeedLimits: SetPTPJointSpeedLimits,
  SetWorkpiece: SetWorkpiece,
  TimeToDestination: TimeToDestination,
  SetSmartServoLinSpeedLimits: SetSmartServoLinSpeedLimits,
  SetSpeedOverride: SetSpeedOverride,
  SetEndpointFrame: SetEndpointFrame,
  ConfigureControlMode: ConfigureControlMode,
  SetSmartServoJointSpeedLimits: SetSmartServoJointSpeedLimits,
};
