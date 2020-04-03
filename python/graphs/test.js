const node = {};
const commonProperties = [
  'first_name',
  'last_name',
  'known_as',
];
const careerNavigationProperties = [
  ...commonProperties,

];
const vesselTransferProperties = [

];
const rehireProperties = [
  
]
let currentProperties;
if (this.optionSelected === 'vessel') { currentProperties = vesselTransferProperties; }
if (this.optionSelected === 'career') { currentProperties = careerNavigationProperties; }
if (this.optionSelected === 'rehire') { currentProperties = rehireProperties; }
const pickedObject = pick(node.data, currentProperties)