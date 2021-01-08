import simtk.unit as unit

class AlanineDipeptideVacuum():

    """Alanine dipeptide in vacuum

    Alanine dipeptide same as OpenMMTools


    Attributes
    ----------
    system
        Xxx xxx

    Methods
    -------

    """

    def __init__(self, forcefield='AMBER96', constraints='h_bonds', hydrogen_mass=None):

        """XXX

        A new test system is returned with the openmm system of particles in an external double
        well potential.

        Parameters
        ----------

        forcefield: xxx
            XXX
        constraints: app.Hbonds
            XXX
        hydrogen_mass: None
            XXX

        Examples
        --------

        >>> from uibcdf_test_systems.systems import AlanineDipeptideVacuum
        >>> from simtk import unit
        >>> dialanine = AlanineDipeptideVacuum(forcefield='xxx')

        Notes
        -----

        See `corresponding documentation in the user guide regarding this class
        <../../systems/dialanine.html>`_.

        """

        # Parameters

        self.parameters={}
        self.parameters['forcefield']=forcefield
        self.parameters['constraints']=constraints
        self.parameters['hydrogen_mass']=hydrogen_mass

        # openmm.Modeller

        from molsysmt import convert
        from .files import alanine_dipeptide
        file_pdb = alanine_dipeptide['vacuum.pdb']
        item_modeller = convert(file_pdb, to_form='openmm.Modeller')

        # OpenMM topology

        self.topology = item_modeller.topology

        # Coordinates

        self.coordinates = item_modeller.positions

        # OpenMM system

        self.system = convert(item_modeller, to_form='openmm.System', forcefield=forcefield,
                              constraints=constraints, hydrogen_mass=hydrogen_mass,
                              implicit_solvent=None, non_bonded_method='no_cutoff')

class AlanineDipeptideImplicitSolvent():

    """Alanine dipeptide in implicit solvent

    Alanine dipeptide same as OpenMMTools


    Attributes
    ----------
    system
        Xxx xxx
    positions
        Xxx xxx
    topology
        Xxx xxx

    Methods
    -------

    """

    def __init__(self, forcefield='AMBER96', implicit_solvent='obc1', solute_dielectric=1.0,
                 solvent_dielectric=78.3, implicit_solvent_kappa=0.0/unit.nanometer,
                 constraints='h_bonds', hydrogen_mass=None):

        """Creating a new instance of AlanineDipeptideImplicitSolvent

        ...

        Parameters
        ----------

        forcefield: xxx
            XXX
        constraints: app.Hbonds
            XXX
        hydrogen_mass: None
            XXX

        Examples
        --------

        >>> from uibcdf_test_systems.systems import AlanineDipeptideImplicitSolvent
        >>> from simtk import unit
        >>> dialanine = AlanineDipeptideImplicitSolvent(forcefield='xxx')

        Notes
        -----

        See `corresponding documentation in the user guide regarding this class
        <../../systems/dialanine.html>`_.

        """

        # Parameters

        self.parameters={}
        self.parameters['forcefield']=forcefield
        self.parameters['constraints']=constraints
        self.parameters['hydrogen_mass']=hydrogen_mass

        # openmm.Modeller

        from molsysmt import convert
        from .files import alanine_dipeptide
        file_pdb = alanine_dipeptide['vacuum.pdb']
        item_modeller = convert(file_pdb, to_form='openmm.Modeller')

        # OpenMM topology

        self.topology = item_modeller.topology

        # Coordinates

        self.coordinates = item_modeller.positions

        # OpenMM system

        self.system = convert(item_modeller, to_form='openmm.System', forcefield=forcefield,
                              constraints=constraints, hydrogen_mass=hydrogen_mass, non_bonded_method='no_cutoff',
                              implicit_solvent=implicit_solvent, solute_dielectric=solute_dielectric,
                              solvent_dielectric=solvent_dielectric, implicit_solvent_kappa=implicit_solvent_kappa
                             )

#class AlanineDipeptideExplicitSolvent():
#
#    """Alanine dipeptide in explicit solvent
#
#    Alanine dipeptide same as OpenMMTools
#
#
#    Attributes
#    ----------
#    system
#        Xxx xxx
#    positions
#        Xxx xxx
#    topology
#        Xxx xxx
#
#    Methods
#    -------
#
#    """
#
#    system = None
#    positions = None
#    topology = None
#
#    def __init__(self, forcefield = 'AMBER96', water_model = 'TIP3P', rigid_water = True, constraints = app.HBonds,
#                 nonbonded_cutoff = 10.0 * unit.angstroms, use_dispersion_correction = True, nonbonded_method = app.PME,
#                 hydrogen_mass = None, switch_width = 1.5 * unit.angstroms, ewald_error_tolerance = 1.0e-5):
#
#        """Creating a new instance of AlanineDipeptideExplicitSolvent
#
#        clearance: 10 angstroms and box_geometry: truncated_octahedral
#
#        Parameters
#        ----------
#
#        forcefield: xxx
#            XXX
#        constraints: app.Hbonds
#            XXX
#        hydrogen_mass: None
#            XXX
#
#        Examples
#        --------
#
#        >>> from uibcdf_test_systems.systems import AlanineDipeptideExplicitSolvent
#        >>> from simtk import unit
#        >>> dialanine = AlanineDipeptideExplicitSolvent()
#
#        Notes
#        -----
#
#        See `corresponding documentation in the user guide regarding this class
#        <../../systems/dialanine.html>`_.
#
#        """
#
#        # OpenMM system
#
#        """ How these files were created:
#
#            import molsysmt as msm
#            sequence = 'seq3:AceAlaNme'
#            msm.build_peptide(sequence, forcefield='AMBER96', to_form=['dialanine_amber96_vacuum.prmtop','dialaninen_amber96_vacuum.inpcrd'])
#        """
#
#        import pathlib
#        dirdata = pathlib.Path(__file__).parent.absolute()
#
#        if forcefield=='AMBER96' and water_model=='TIP3P':
#            prmtop_filepath = pathlib.PurePath(dirdata).joinpath('dialanine_amber96_tip3p.prmtop')
#            inpcrd_filepath = pathlib.PurePath(dirdata).joinpath('dialanine_amber96_tip3p.inpcrd')
#        else:
#            raise NotImplementedError('The system was not implemented yet with this forcefield.')
#
#        amber_prmtop_file = app.AmberPrmtopFile(prmtop_filepath)
#        amber_inpcrd_file = app.AmberInpcrdFile(inpcrd_filepath)
#
#        self.topology = amber_prmtop_file.topology
#        self.positions = amber_inpcrd_file.getPositions(asNumpy=True)
#        self.system = amber_prmtop_file.createSystem(constraints=constraints, nonbondedMethod=nonbonded_method,
#                                                     rigidWater=rigid_water, nonbondedCutoff=nonbonded_cutoff,
#                                                     hydrogenMass=hydrogen_mass)
#
#        box_vectors = amber_inpcrd_file.getBoxVectors(asNumpy=True)
#        self.system.setDefaultPeriodicBoxVectors(box_vectors[0], box_vectors[1], box_vectors[2])
#
#        # Dispersion correction.
#        forces = {self.system.getForce(index).__class__.__name__: self.system.getForce(index) for index in range(self.system.getNumForces())}
#        forces['NonbondedForce'].setUseDispersionCorrection(use_dispersion_correction)
#        forces['NonbondedForce'].setEwaldErrorTolerance(ewald_error_tolerance)
#
#        # Switch width.
#        if switch_width is not None:
#            forces['NonbondedForce'].setUseSwitchingFunction(True)
#            forces['NonbondedForce'].setSwitchingDistance(nonbonded_cutoff - switch_width)
#
