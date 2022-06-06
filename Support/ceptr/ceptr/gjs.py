"""Gauss-Jordan functions."""
import ceptr.writer as cw


def emptygjs(fstream):
    """Write an empty gauss-jordan solver."""
    cw.writer(fstream)
    cw.writer(fstream, cw.comment("gauss-jordan solver external routine"))
    cw.writer(
        fstream,
        cw.comment(
            "Replace this routine with the one generated by the Gauss Jordan"
            " solver of DW"
        ),
    )
    cw.writer(
        fstream,
        "AMREX_GPU_HOST_DEVICE AMREX_FORCE_INLINE void sgjsolve(amrex::Real*"
        " /*A*/, amrex::Real* /*x*/, amrex::Real* /*b*/) {",
    )
    cw.writer(
        fstream,
        'amrex::Abort("sgjsolve not implemented, choose a different'
        ' solver ");',
    )
    cw.writer(fstream, "}")

    cw.writer(fstream)
    cw.writer(
        fstream,
        cw.comment(
            "Replace this routine with the one generated by the Gauss Jordan"
            " solver of DW"
        ),
    )
    cw.writer(
        fstream,
        "AMREX_GPU_HOST_DEVICE AMREX_FORCE_INLINE void"
        " sgjsolve_simplified(amrex::Real* /*A*/, amrex::Real* /*x*/,"
        " amrex::Real* /*b*/) {",
    )
    cw.writer(
        fstream,
        'amrex::Abort("sgjsolve_simplified not implemented, choose a different'
        ' solver ");',
    )
    cw.writer(fstream, "}")